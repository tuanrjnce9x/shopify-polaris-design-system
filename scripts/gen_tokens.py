import json, re
B='/private/tmp/claude-501/-Users-will-second-brain/56790265-d246-44e6-a02d-a0051c52481d/scratchpad/polaris-ds/'
T=json.load(open(B+'src/themes.json'))['light']
def rgba(v):
    m=re.match(r'rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)',v)
    return [float(x) for x in m.groups(default='1')]
def lum(c):
    def ch(x):
        x/=255; return x/12.92 if x<=0.03928 else ((x+0.055)/1.055)**2.4
    return 0.2126*ch(c[0])+0.7152*ch(c[1])+0.0722*ch(c[2])
def blend(fg,bg):
    a=fg[3]; return [fg[i]*a+bg[i]*(1-a) for i in range(3)]+[1]
def cr(a,b):
    la,lb=lum(a),lum(b); return (max(la,lb)+0.05)/(min(la,lb)+0.05)
def tohex(v):
    r,g,b,a=rgba(v); h='#%02x%02x%02x'%(round(r),round(g),round(b))
    if a<1: h+='%02x'%round(a*255)
    return h
C=T['color']
extra={
 'color-avatar-bg-fill':'Avatar background when no initials colour applies.',
 'color-avatar-text-on-bg-fill':'Initials on color-avatar-bg-fill.',
 'color-backdrop-bg':'Scrim behind modals and sheets.',
 'color-checkbox-bg-surface-disabled':'Disabled checkbox fill.',
 'color-checkbox-icon-disabled':'Check mark on a disabled checked checkbox.',
 'color-input-bg-surface':'Text field, select and checkbox background at rest.',
 'color-input-bg-surface-hover':'Input background on hover.',
 'color-input-bg-surface-active':'Input background while focused.',
 'color-input-border':'Input border at rest (0.04125rem / 0.66px hairline). 3.4:1 on white.',
 'color-input-border-hover':'Input border on hover.',
 'color-input-border-active':'Input border while focused (with the focus outline).',
 'color-nav-bg':'Admin left navigation background.',
 'color-nav-bg-surface':'Navigation item at rest.',
 'color-nav-bg-surface-hover':'Navigation item on hover.',
 'color-nav-bg-surface-active':'Navigation item while pressed.',
 'color-nav-bg-surface-selected':'Selected navigation item.',
 'color-radio-button-bg-surface-disabled':'Disabled radio fill.',
 'color-radio-button-icon-disabled':'Dot of a disabled selected radio.',
 'color-video-thumbnail-play-button-bg-fill':'Play button on video thumbnails.',
 'color-video-thumbnail-play-button-bg-fill-hover':'Play button on hover.',
 'color-video-thumbnail-play-button-text-on-bg-fill':'Play glyph on the play button.',
 'color-scrollbar-thumb-bg':'Scrollbar thumb.',
 'color-scrollbar-thumb-bg-hover':'Scrollbar thumb on hover.',
 'color-tooltip-tail-down-border':'Border of a tooltip tail pointing down.',
 'color-tooltip-tail-up-border':'Border of a tooltip tail pointing up.',
}
white=rgba(C['color-bg-surface']['value']); page=rgba(C['color-bg']['value'])
colors=[];skipped=[]
for k,v in C.items():
    val=v['value']
    if not val.startswith('rgb'): skipped.append(k); continue
    u=v.get('description') or extra.get(k)
    if not u:
        m=re.match(r'color-avatar-(\w+)-(bg-fill|text-on-bg-fill)',k)
        if m: u=('Avatar colour %s background.'%m.group(1)) if m.group(2)=='bg-fill' else ('Initials on color-avatar-%s-bg-fill.'%m.group(1))
    assert u,k
    fg=rgba(val)
    if k.startswith('color-text') and 'on-bg-fill' not in k and 'inverse' not in k:
        a=cr(blend(fg,white),white); b=cr(blend(fg,page),page)
        note=' Reads on bg-surface (%.1f:1) and bg (%.1f:1).'%(a,b)
        if a>=4.5 and b<4.5 and 'disabled' not in k: note+=' Below 4.5:1 on bg in the source: use it on surfaces (cards), not on the bare page background.'
        elif min(a,b)<4.5: note+=' Below 4.5:1 in the source: keep for disabled/large text only.' if 'disabled' in k else ' Below 4.5:1 on these grounds in the source: use at 24px+ or for non-text marks.'
        u=u.rstrip('.')+'.'+note
    colors.append({'name':'p-'+k,'value':tohex(val),'usage':u})
def lst(fam, pref, usage, conv=None):
    out=[]
    for k,v in T[fam].items():
        if pref and not k.startswith(pref): continue
        val=v['value']
        mm=re.match(r'var\(--p-([\w-]+)\)',val)
        if mm: val=T[fam][mm.group(1)]['value']
        out.append({'name':'p-'+k,'value':val,'usage':usage(k,val)})
    return out
def px(val):
    m=re.match(r'(-?[\d.]+)rem',val); return ('%gpx'%(float(m.group(1))*16)) if m else val
spaceuse={'space-025':'Hairline offsets; focus outline offset.','space-050':'Button icon-to-label gap; badge vertical padding.','space-100':'Label-to-field gap; tight inline gaps.','space-150':'Control vertical padding (buttons, inputs); table cell padding.','space-200':'Badge horizontal padding; button group gap; table cell vertical padding.','space-300':'Control horizontal padding; banner padding.','space-400':'Card padding and gap between cards; modal padding.','space-500':'Page gutters on small screens.','space-600':'Page header vertical padding on desktop.','space-800':'Wide page gutters; large section gaps.','space-button-group-gap':'Gap between buttons in a group (= space-200).','space-card-gap':'Gap between stacked cards (= space-400).','space-card-padding':'Inner padding of a card (= space-400).','space-table-cell-padding':'Table cell padding (= space-150).'}
spacing=lst('space','space-',lambda k,v: '%s (%s). %s'%(v,px(v),spaceuse.get(k,'Layout spacing step.')))
raduse={'border-radius-0':'Square corners (banners on mobile).','border-radius-050':'Tiny marks.','border-radius-100':'Checkboxes, progress bar, toast (legacy).','border-radius-150':'Extra-small thumbnails; link focus ring.','border-radius-200':'Buttons, inputs, selects, badges, thumbnails, tabs, toasts.','border-radius-300':'Cards (sections) and page-level banners.','border-radius-400':'Modals.','border-radius-500':'Large surfaces.','border-radius-750':'Extra-large surfaces.','border-radius-full':'Pills, radios, avatars, switches.'}
radius=lst('border','border-radius-',lambda k,v:'%s (%s). %s'%(v,px(v),raduse.get(k,'')))
bwuse={'border-width-0':'No border.','border-width-0165':'Input, select, checkbox and radio hairline (0.66px).','border-width-025':'Standard 1px border: dividers, table rows, modal header/footer.','border-width-050':'Focus outline width (2px, color-border-focus).','border-width-100':'Heavy 4px rule.'}
bw=lst('border','border-width-',lambda k,v:'%s (%s). %s'%(v,px(v),bwuse[k]))
shuse={'shadow-0':'No elevation.','shadow-100':'Cards (sections) at rest, with shadow-bevel-100.','shadow-200':'Page-level banners.','shadow-300':'Raised elements: popovers at rest.','shadow-400':'Toasts and popovers.','shadow-500':'Floating menus.','shadow-600':'Modals.','shadow-bevel-100':'Inset bevel drawn over cards, banners and toasts (::before, mix-blend-mode luminosity).','shadow-inset-100':'Pressed inset.','shadow-inset-200':'Deeper pressed inset.','shadow-button':'Secondary button at rest.','shadow-button-hover':'Secondary button on hover.','shadow-button-inset':'Secondary button while pressed.','shadow-button-primary':'Primary button at rest.','shadow-button-primary-hover':'Primary button on hover.','shadow-button-primary-inset':'Primary button while pressed.','shadow-button-primary-critical':'Critical primary button at rest.','shadow-button-primary-critical-hover':'Critical primary button on hover.','shadow-button-primary-critical-inset':'Critical primary button while pressed.','shadow-button-primary-success':'Success primary button (save bar Save) at rest.','shadow-button-primary-success-hover':'Success primary button on hover.','shadow-button-primary-success-inset':'Success primary button while pressed.','shadow-border-inset':'1px inner border on thumbnails and images.'}
shadow=lst('shadow','',lambda k,v:shuse[k])
fuse={'font-size':'Font size step','font-weight':'Font weight','font-letter-spacing':'Letter spacing','font-line-height':'Line height step'}
def fu(k,v):
    for p,s in fuse.items():
        if k.startswith(p):
            extra={'font-weight-regular':'Body text (variable Inter 450).','font-weight-medium':'Button labels, badges, table headings.','font-weight-semibold':'Headings md and below, headingLg.','font-weight-bold':'Page title (headingLg bold), heading xl–3xl.','font-size-325':'13px: body text and inputs on desktop.','font-size-300':'12px: badges, small buttons labels, table headings.','font-size-350':'14px: headingMd, bodyLg.','font-size-400':'16px: inputs on mobile (prevents iOS zoom).','font-size-500':'20px: headingLg, page title.'}.get(k,'')
            return ('%s: %s%s. %s'%(s,v,(' (%s)'%px(v)) if 'rem' in v else '',extra)).strip()
font=lst('font','font-',fu)
font=[t for t in font if not t['name'].startswith('p-font-family')]
zuse=lambda k,v:'Stacking layer %s (Polaris z-index scale; modals use z-index-11).'%v
z=lst('zIndex','',zuse)
bp=lst('breakpoints','',lambda k,v:'%s (%s). Min-width breakpoint for media queries: xs phones, sm 490px, md 768px (desktop controls), lg 1040px, xl 1440px.'%(v,px(v)))
hgt=lst('height','',lambda k,v:'%s (%s). Fixed heights; control min-height uses height-800 mobile / height-700 desktop for buttons.'%(v,px(v)))
wdt=lst('width','',lambda k,v:'%s (%s). Fixed widths; mirrors the height scale.'%(v,px(v)))
def style(name,key,sample,usage):
    p='text-%s-font-'%key; g=lambda s: T['font'][re.match(r'var\(--p-([\w-]+)\)',T['text'][p+s]['value']).group(1)]['value']
    return {'name':name,'fontSize':g('size'),'lineHeight':g('line-height'),'fontWeight':int(g('weight')),'letterSpacing':g('letter-spacing'),'sample':sample,'usage':usage}
heads=[style('heading3xl','heading-3xl','Welcome to your store','Rare hero numbers or onboarding headlines. 36px/48px bold.'),
 style('heading2xl','heading-2xl','$12,480 in sales','Large dashboard metrics. 30px/40px bold.'),
 style('headingXl','heading-xl','Set up your loyalty program','Empty-state or onboarding headings. 24px/32px bold.'),
 style('headingLg','heading-lg','Products','Page titles (the Page component renders it bold, 700). 20px/24px.'),
 style('headingMd','heading-md','Shipping and delivery','Section (card) and modal headings. 14px/20px semibold.'),
 style('headingSm','heading-sm','Order details','Banner headings and nested section headings. 13px/20px semibold.'),
 style('headingXs','heading-xs','Sales channels','Small group labels. 12px/16px semibold.')]
body=[style('bodyLg','body-lg','Customers will see this message at checkout.','Emphasised paragraphs. 14px/20px.'),
 style('bodyMd','body-md','Your changes are saved automatically when you close this page.','Default body copy, labels, inputs and table cells. 13px/20px.'),
 style('bodySm','body-sm','Last updated 2 minutes ago','Help text, captions, button labels at default size. 12px/16px.'),
 style('bodyXs','body-xs','SKU 2034-RED','Dense metadata only. 11px/12px.')]
fam_sans="\"Inter\", -apple-system, BlinkMacSystemFont, \"San Francisco\", \"Segoe UI\", Roboto, \"Helvetica Neue\", sans-serif"
fam_mono="ui-monospace, SFMono-Regular, \"SF Mono\", Consolas, \"Liberation Mono\", Menlo, monospace"
assert fam_sans.replace('"',"'")==T['font']['font-family-sans']['value'], T['font']['font-family-sans']['value']
assert fam_mono.replace('"',"'")==T['font']['font-family-mono']['value']
tokens={'name':'Shopify Polaris Admin','version':1,
 'meta':{'source':'npm','package':'@shopify/polaris-tokens@9.4.2','theme':'light','components-css':'@shopify/polaris@13.9.5 (Polaris React build CSS, reference for component metrics)','icons':'@shopify/polaris-icons@9.3.1','synced':'2026-11-13'},
 'color':{'themes':[{'id':'light','name':'Light'}],'note':'Polaris light theme (the admin theme). Names match the Polaris CSS custom properties (--p-color-*). Values converted from rgba() to hex.','tokens':colors},
 'type':{'fonts':[],'families':{'sans':fam_sans,'mono':fam_mono},
   'groups':[{'name':'Headings','family':'sans','note':'Polaris text variants headingXs–heading3xl. Inter is variable; weights 450/550/650 need the variable font.','styles':heads},
             {'name':'Body','family':'sans','note':'Polaris text variants bodyXs–bodyLg. bodyMd is the default.','styles':body}]},
 'spacing':{'note':'Polaris space scale; the number is the multiple of 4px ×100 (space-400 = 16px).','tokens':spacing},
 'radius':{'note':'Soft, consistent corners: 8px controls, 12px cards, 16px modals.','tokens':radius},
 'shadow':{'note':'Subtle elevation plus bevel and button shadows that give Polaris buttons their 3D edge.','tokens':shadow},
 'borderWidth':{'note':'Border widths.','tokens':bw},
 'fontScale':{'note':'Raw font scale behind the text variants, as CSS variables for previews and code.','tokens':font},
 'height':{'tokens':hgt},'width':{'tokens':wdt},
 'zIndex':{'tokens':z},'breakpoints':{'tokens':bp}}
names=[t['name'] for f in tokens if isinstance(tokens[f],dict) and 'tokens' in tokens[f] for t in tokens[f]['tokens']]
assert len(names)==len(set(names)); assert all(re.match(r'^[A-Za-z0-9][A-Za-z0-9_.-]{0,63}$',n) for n in names)
json.dump(tokens,open(B+'project/tokens.json','w'),indent=1,ensure_ascii=False)
print('colors',len(colors),'skipped',skipped,'space',len(spacing),'radius',len(radius),'bw',len(bw),'shadow',len(shadow),'font',len(font),'z',len(z),'bp',len(bp),'h',len(hgt),'w',len(wdt))
for c in colors:
    if 'Below' in c['usage']: print(c['name'],c['usage'][-120:])

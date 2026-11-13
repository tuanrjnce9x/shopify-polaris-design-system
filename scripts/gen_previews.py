import os, re
B='/private/tmp/claude-501/-Users-will-second-brain/56790265-d246-44e6-a02d-a0051c52481d/scratchpad/polaris-ds/'
ICON=B+'src/icons/package/dist/svg/'
SPIN='<span class="pl-spinner" role="status" aria-label="Loading"><svg viewBox="0 0 20 20"><path d="M7.229 1.173a9.25 9.25 0 1011.655 11.412 1.25 1.25 0 10-2.4-.698 6.75 6.75 0 11-8.506-8.329 1.25 1.25 0 10-.75-2.385z"/></svg></span>'
def icon(m):
    name, cls = m.group(1), (m.group(2) or '')
    svg=open(ICON+name+'Icon.svg').read().strip().replace(' xmlns="http://www.w3.org/2000/svg"','')
    return '<span class="pl-icon%s" aria-hidden="true">%s</span>'%((' '+cls) if cls else '', svg)
def render(s):
    s=s.replace('{{spinner}}',SPIN)
    return re.sub(r'\{\{i:(\w+)(?:\s+([\w -]+))?\}\}', icon, s)
HEAD='''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>%s</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@100..900&display=swap">%s
</head>
<body>
%s
</body>
</html>
'''
P={}
def card(name, group, height, body, style='', subtitle=None, page=False):
    marker='<!-- @dsCard group="%s" height=%d%s%s -->'%(group,height,(' subtitle="%s"'%subtitle) if subtitle else '',' page' if page else '')
    P[name]=marker+'\n'+HEAD%(name, ('\n<style>%s</style>'%style) if style else '', render(body))

card('Button','Actions',176,'''<div class="pl-pad pl-col-tight">
<div class="pl-row">
<button class="pl-btn pl-btn--primary">Save</button>
<button class="pl-btn">Preview</button>
<button class="pl-btn pl-btn--tertiary">Cancel</button>
<button class="pl-btn pl-btn--icon-text">{{i:Plus}}Add product</button>
<button class="pl-btn pl-btn--tertiary pl-btn--icon-only" aria-label="Edit product">{{i:Edit}}</button>
</div>
<div class="pl-row">
<button class="pl-btn pl-btn--primary pl-btn--critical">Delete campaign</button>
<button class="pl-btn pl-btn--critical">{{i:Delete}}Remove</button>
<button class="pl-btn pl-btn--primary pl-btn--loading" aria-busy="true">Saving{{spinner}}</button>
<button class="pl-btn pl-btn--primary" disabled>Save</button>
<button class="pl-btn" disabled>Export</button>
</div>
<div class="pl-row">
<button class="pl-btn pl-btn--primary pl-btn--large">Install app</button>
<button class="pl-btn pl-btn--large">Learn more</button>
</div>
</div>''')

card('Link','Actions',72,'''<div class="pl-pad pl-col-tight">
<p class="pl-body-md">Customers can track orders from the <a class="pl-link" href="#">order status page</a>.</p>
<p class="pl-body-md pl-subdued">Need help? <a class="pl-link pl-link--monochrome" href="#">Contact support</a></p>
</div>''')

card('Badge','Feedback',120,'''<div class="pl-pad pl-col-tight">
<div class="pl-row">
<span class="pl-badge">Draft</span>
<span class="pl-badge pl-badge--info">Scheduled</span>
<span class="pl-badge pl-badge--success">Active</span>
<span class="pl-badge pl-badge--caution">Unfulfilled</span>
<span class="pl-badge pl-badge--warning">Payment pending</span>
<span class="pl-badge pl-badge--critical">Failed</span>
</div>
<div class="pl-row">
<span class="pl-badge pl-badge--success pl-badge--strong">Paid</span>
<span class="pl-badge pl-badge--critical pl-badge--strong">Action required</span>
<span class="pl-badge pl-badge--success pl-badge--large">{{i:CheckCircle}}Enabled</span>
<span class="pl-badge pl-badge--warning pl-badge--large">Partially refunded</span>
</div>
</div>''')

card('Banner','Feedback',420,'''<div class="pl-pad pl-col">
<div class="pl-banner pl-banner--info" role="status">
<div class="pl-banner__head"><div class="pl-banner__title">{{i:Info}}<span>App embed is turned off</span></div><button class="pl-btn pl-btn--tertiary pl-btn--icon-only" aria-label="Dismiss">{{i:X}}</button></div>
<div class="pl-banner__body"><p>Turn on the app embed in your theme editor so the widget appears on your storefront.</p><div class="pl-btn-group"><button class="pl-btn">Open theme editor</button></div></div>
</div>
<div class="pl-banner pl-banner--warning" role="status">
<div class="pl-banner__head"><div class="pl-banner__title">{{i:AlertTriangle}}<span>127 products missing shipping weights</span></div></div>
<div class="pl-banner__body"><p>Products without weights may show inaccurate shipping rates.</p></div>
</div>
<div class="pl-card pl-col-tight">
<h2 class="pl-heading-md">Inside a section</h2>
<div class="pl-inline-banner pl-inline-banner--success">{{i:CheckCircle}}<p>Your settings were saved.</p></div>
<div class="pl-inline-banner pl-inline-banner--critical">{{i:AlertCircle}}<p>We couldn’t connect to your account. Try again in a few minutes.</p></div>
</div>
</div>''')

card('Progress','Feedback',120,'''<div class="pl-pad pl-col-tight" style="max-width:420px">
<div class="pl-spread"><span>Importing products</span><span class="pl-subdued">3 of 5</span></div>
<div class="pl-progress" role="progressbar" aria-label="Importing products" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100"><div class="pl-progress__bar" style="width:60%"></div></div>
<div class="pl-progress pl-progress--small pl-progress--success" role="progressbar" aria-label="Setup complete" aria-valuenow="100"><div class="pl-progress__bar" style="width:100%"></div></div>
</div>''')

card('EmptyState','Feedback',300,'''<div class="pl-pad"><div class="pl-card">
<div class="pl-empty">
<div class="pl-empty__graphic">{{i:Product}}</div>
<h2 class="pl-heading-md">Add your first product</h2>
<p class="pl-empty__text">Products you add here are ready to sell across your sales channels.</p>
<div class="pl-btn-group"><button class="pl-btn">Import</button><button class="pl-btn pl-btn--primary">Add product</button></div>
</div></div></div>''')

card('Page','Layout',300,'''<div class="pl-page pl-page--small" style="padding-bottom:16px">
<div class="pl-page__header">
<div class="pl-page__title"><button class="pl-btn pl-btn--tertiary pl-btn--icon-only" aria-label="Back">{{i:ArrowLeft}}</button><h1>Loyalty settings</h1><span class="pl-badge pl-badge--success">Active</span></div>
<div class="pl-btn-group"><button class="pl-btn">Preview</button><button class="pl-btn pl-btn--primary">Save</button></div>
</div>
<div class="pl-col">
<div class="pl-card"><div class="pl-card__head"><h2 class="pl-heading-md">Points</h2></div><p class="pl-subdued">Customers earn 1 point for every $1 spent.</p></div>
<div class="pl-card"><div class="pl-card__head"><h2 class="pl-heading-md">Rewards</h2><button class="pl-btn pl-btn--tertiary">Edit</button></div><p class="pl-subdued">3 rewards available</p></div>
</div></div>''')

card('Section','Layout',260,'''<div class="pl-pad pl-col" style="max-width:560px">
<section class="pl-card">
<div class="pl-card__head"><h2 class="pl-heading-md">Widget appearance</h2><button class="pl-btn pl-btn--tertiary">Reset</button></div>
<p class="pl-subdued">Choose how the widget looks on your product pages.</p>
<hr class="pl-divider" style="margin:16px -16px">
<div class="pl-spread"><span>Position</span><span class="pl-subdued">Below add to cart</span></div>
</section>
<section class="pl-card"><div class="pl-card__head"><h2 class="pl-heading-md">Status</h2><span class="pl-badge pl-badge--success">On</span></div><p>Visible to customers.</p></section>
</div>''')

card('Stack','Layout',150,'''<div class="pl-pad pl-col-tight" style="max-width:560px">
<div class="pl-row" style="gap:var(--p-space-200)"><div class="demo">small-100</div><div class="demo">8px</div><div class="demo">gap</div></div>
<div class="pl-row" style="gap:var(--p-space-400)"><div class="demo">base</div><div class="demo">16px</div><div class="demo">gap</div></div>
<hr class="pl-divider">
<div class="pl-spread"><span class="pl-heading-sm">justifyContent: space-between</span><span class="pl-badge">inline</span></div>
</div>''', style='.demo{padding:var(--p-space-200) var(--p-space-300);background:var(--p-color-bg-surface);border-radius:var(--p-border-radius-200);box-shadow:var(--p-shadow-100)}')

def row(img,title,sub,badge,tone,amt):
    return '<tr><td><span class="pl-choice__control" style="display:inline-block;vertical-align:middle;margin:0"><span class="pl-checkbox"></span></span></td><td><div class="pl-row" style="flex-wrap:nowrap"><span class="pl-thumb pl-thumb--xs"><span class="pl-thumb__fill" style="background:%s"></span></span><span class="pl-medium">%s</span></div></td><td class="pl-subdued">%s</td><td><span class="pl-badge pl-badge--%s">%s</span></td><td class="pl-num">%s</td></tr>'%(img,title,sub,tone,badge,amt)
card('Table','Layout',330,'''<div class="pl-pad"><div class="pl-card pl-card--flush">
<ul class="pl-tabs"><li class="pl-tab pl-tab--active">All</li><li class="pl-tab">Active</li><li class="pl-tab">Draft</li></ul>
<table class="pl-table"><thead><tr><th style="width:20px"></th><th>Product</th><th>Inventory</th><th>Status</th><th class="pl-num">Price</th></tr></thead><tbody>
'''+row('#e3e3e3','Linen shirt','24 in stock','Active','success','$48.00')+row('#cce3f5','Canvas tote','0 in stock','Out of stock','critical','$22.00')+row('#f1e7d0','Wool beanie','8 in stock','Draft','info','$18.00')+'''
</tbody></table>
<div class="pl-table__footer"><button class="pl-btn pl-btn--tertiary pl-btn--icon-only" aria-label="Previous" disabled>{{i:ChevronLeft}}</button><button class="pl-btn pl-btn--tertiary pl-btn--icon-only" aria-label="Next">{{i:ChevronRight}}</button></div>
</div></div>''')

card('TextField','Forms',250,'''<div class="pl-pad pl-col-tight" style="max-width:420px">
<div class="pl-field"><label class="pl-label">Store name</label><div class="pl-input"><input value="Linen &amp; Co"></div><p class="pl-help">Appears in emails and on your storefront.</p></div>
<div class="pl-field"><label class="pl-label pl-label--required">Discount</label><div class="pl-input pl-input--focus"><input value="15"><span class="pl-input__suffix">%</span></div></div>
<div class="pl-field"><label class="pl-label">Email</label><div class="pl-input pl-input--error"><input value="hello@"></div><div class="pl-error">{{i:AlertCircle}}<span>Enter a valid email address</span></div></div>
</div>''')

card('Select','Forms',100,'''<div class="pl-pad" style="max-width:420px"><div class="pl-field pl-select"><label class="pl-label">Widget position</label><div class="pl-input"><span class="pl-input__value">Below add to cart button</span>{{i:Select}}</div></div></div>''')

card('Checkbox','Forms',110,'''<div class="pl-pad pl-col-tight">
<label class="pl-choice"><span class="pl-choice__control"><span class="pl-checkbox pl-checkbox--checked">{{i:Check}}</span></span><span>Show on product pages</span></label>
<label class="pl-choice"><span class="pl-choice__control"><span class="pl-checkbox"></span></span><span>Show on collection pages</span></label>
<label class="pl-choice pl-choice--disabled"><span class="pl-choice__control"><span class="pl-checkbox"></span></span><span>Show on checkout (Shopify Plus only)</span></label>
</div>''')

card('Switch','Forms',96,'''<div class="pl-pad pl-col-tight">
<label class="pl-choice" style="align-items:center"><span class="pl-switch pl-switch--on"></span><span>Enable notifications</span></label>
<label class="pl-choice" style="align-items:center"><span class="pl-switch"></span><span>Send weekly summary</span></label>
</div>''')

card('ChoiceList','Forms',150,'''<div class="pl-pad"><fieldset class="pl-choice-list"><legend>Reward type</legend>
<label class="pl-choice"><span class="pl-choice__control"><span class="pl-radio pl-radio--checked"></span></span><span>Percentage off</span></label>
<label class="pl-choice"><span class="pl-choice__control"><span class="pl-radio"></span></span><span>Fixed amount off</span></label>
<label class="pl-choice"><span class="pl-choice__control"><span class="pl-radio"></span></span><span>Free shipping</span></label>
<p class="pl-choice__help">Applies to the next order only.</p>
</fieldset></div>''')

card('ColorField','Forms',100,'''<div class="pl-pad" style="max-width:320px"><div class="pl-field"><label class="pl-label">Button background color</label><div class="pl-input"><span class="pl-swatch" style="background:#005bd3"></span><input value="#005BD3"></div></div></div>''')

card('Modal','Overlays',300,'''<div class="pl-backdrop"><div class="pl-modal pl-modal--small" role="dialog" aria-label="Delete reward?">
<div class="pl-modal__head"><h2 class="pl-heading-md">Delete reward?</h2><button class="pl-btn pl-btn--tertiary pl-btn--icon-only" aria-label="Close">{{i:X}}</button></div>
<div class="pl-modal__body"><p>Customers who haven’t redeemed “10% off” will lose access to it. This can’t be undone.</p></div>
<div class="pl-modal__foot"><button class="pl-btn">Cancel</button><button class="pl-btn pl-btn--primary pl-btn--critical">Delete reward</button></div>
</div></div>''', style='body{background:var(--p-color-bg)}')

card('SaveBar','App Bridge',72,'''<div class="pl-savebar"><div class="pl-row">{{i:AlertTriangle pl-icon--warning}}<h2 class="pl-heading-md">Unsaved changes</h2></div>
<div class="pl-btn-group"><button class="pl-btn pl-btn--tertiary pl-btn--large">Discard</button><button class="pl-btn pl-btn--primary pl-btn--success pl-btn--large">Save</button></div></div>''', style='.pl-savebar .pl-icon--warning{fill:var(--p-color-icon-warning)}')

card('Toast','App Bridge',120,'''<div class="pl-pad pl-col-tight" style="align-items:flex-start">
<div class="pl-toast" role="status"><span>Settings saved</span><button class="pl-btn pl-btn--tertiary pl-btn--icon-only" aria-label="Dismiss" style="margin:-4px">{{i:X pl-icon--inverse}}</button></div>
<div class="pl-toast pl-toast--error" role="alert"><span>Couldn’t save settings</span><span class="pl-toast__action">Retry</span></div>
</div>''', style='.pl-toast .pl-btn--tertiary:hover{background:var(--p-color-bg-fill-inverse-hover)}')

names=['Home','Order','Product','Cart','Apps','Settings','View','Search','Plus','Edit','Delete','X','Check','CheckCircle','Info','AlertCircle','AlertTriangle','QuestionCircle','ChevronDown','Select','Menu','Image']
card('Icon','Media',170,'<div class="pl-pad"><div class="grid">'+''.join('<div class="cell">{{i:%s}}<span class="pl-body-xs pl-subdued">%s</span></div>'%(n,n) for n in names)+'</div><div class="pl-row" style="margin-top:12px">{{i:CheckCircle pl-icon--success}}{{i:Info pl-icon--info}}{{i:AlertTriangle pl-icon--warning}}{{i:AlertCircle pl-icon--critical}}{{i:QuestionCircle pl-icon--secondary}}</div></div>',
     style='.grid{display:grid;grid-template-columns:repeat(11,minmax(0,1fr));gap:8px}.cell{display:flex;flex-direction:column;align-items:center;gap:4px;padding:6px 0;text-align:center}')

card('Thumbnail','Media',110,'''<div class="pl-pad pl-row" style="align-items:flex-end;gap:16px">
<span class="pl-thumb pl-thumb--xs"><span class="pl-thumb__fill" style="background:#cce3f5"></span></span>
<span class="pl-thumb"><span class="pl-thumb__fill" style="background:#f1e7d0"></span></span>
<span class="pl-thumb pl-thumb--md">{{i:Image}}</span>
<span class="pl-thumb pl-thumb--lg"><span class="pl-thumb__fill" style="background:#e3e3e3"></span></span>
</div>''')

card('Text','Typography',330,'''<div class="pl-pad pl-col-tight">
<p class="pl-heading-2xl">$12,480</p>
<p class="pl-heading-xl">Set up your loyalty program</p>
<p class="pl-heading-lg">Products</p>
<p class="pl-heading-md">Shipping and delivery</p>
<p class="pl-heading-sm">Order details</p>
<p class="pl-body-lg">Customers will see this message at checkout.</p>
<p class="pl-body-md">Your changes are saved automatically when you close this page.</p>
<p class="pl-body-sm pl-subdued">Last updated 2 minutes ago</p>
<p class="pl-body-md pl-mono">{{ product.title }}</p>
</div>''')

card('AppHomeExample','Examples',560,'''<div class="shell">
<nav class="pl-nav">
<div class="pl-nav__item">{{i:Home}}Home</div>
<div class="pl-nav__item">{{i:Order}}Orders</div>
<div class="pl-nav__item">{{i:Product}}Products</div>
<div class="pl-nav__item" style="margin-top:12px">{{i:Apps}}Apps</div>
<div class="pl-nav__item pl-nav__sub pl-nav__item--selected" style="color:var(--p-color-text)">Loyalty Rewards</div>
<div class="pl-nav__item pl-nav__sub">Dashboard</div>
<div class="pl-nav__item pl-nav__sub">Settings</div>
</nav>
<main class="main">
<div class="pl-page">
<div class="pl-page__header"><div class="pl-page__title"><h1>Dashboard</h1></div><div class="pl-btn-group"><button class="pl-btn">View storefront</button><button class="pl-btn pl-btn--primary">Create reward</button></div></div>
<div class="pl-col">
<div class="pl-banner pl-banner--info"><div class="pl-banner__head"><div class="pl-banner__title">{{i:Info}}<span>Finish setting up</span></div></div><div class="pl-banner__body"><p>Turn on the app embed so customers can see their points.</p><div class="pl-btn-group"><button class="pl-btn">Turn on app embed</button></div></div></div>
<div class="pl-page__layout">
<div class="pl-col">
<section class="pl-card"><div class="pl-card__head"><h2 class="pl-heading-md">Points issued</h2><span class="pl-badge pl-badge--success">+12%</span></div><p class="pl-heading-2xl">48,210</p><p class="pl-subdued">Last 30 days</p></section>
<section class="pl-card pl-col-tight"><h2 class="pl-heading-md">Setup guide</h2><div class="pl-spread"><span class="pl-subdued">2 of 3 tasks complete</span></div><div class="pl-progress pl-progress--small pl-progress--primary"><div class="pl-progress__bar" style="width:66%"></div></div></section>
</div>
<section class="pl-card pl-col-tight"><h2 class="pl-heading-md">Program status</h2><label class="pl-choice" style="align-items:center"><span class="pl-switch pl-switch--on"></span><span>Program active</span></label><p class="pl-subdued">Customers are earning points on every order.</p></section>
</div></div></div>
</main></div>''', style='.shell{display:flex;min-height:560px}.main{flex:1;min-width:0;background:var(--p-color-bg)}', page=True)

card('StorefrontWidgetExample','Examples',260,'''<div class="theme">
<p class="theme-title">Linen shirt</p>
<p class="theme-price">$48.00</p>
<div class="loyalty-widget">
<p class="loyalty-widget__title">Earn 48 points with this purchase</p>
<p>Join our rewards program to redeem points on your next order. <a href="#">Learn more</a></p>
<button type="button" class="loyalty-widget__button">Join now</button>
</div>
</div>''', style='''body{background:#fbf8f3}
/* A stand-in merchant theme: the widget below must take its fonts and colours from here */
.theme{--theme-text:#2d2a26;--theme-accent:#7a3e2b;--theme-radius:2px;font-family:Georgia,"Times New Roman",serif;color:var(--theme-text);padding:24px;max-width:420px}
.theme-title{font-size:22px;margin:0}.theme-price{margin:4px 0 16px}
/* The widget: no Polaris tokens, inherits font and colour, scoped class names */
.loyalty-widget{font:inherit;color:inherit;border:1px solid currentColor;border-radius:var(--theme-radius);padding:12px 16px}
.loyalty-widget p{margin:0 0 8px}.loyalty-widget__title{font-weight:bold}
.loyalty-widget a{color:inherit}
.loyalty-widget__button{font:inherit;color:#fff;background:var(--theme-accent);border:0;border-radius:var(--theme-radius);padding:8px 16px;cursor:pointer}''', subtitle='Not Polaris: inherits the merchant theme')

for n,s in P.items():
    d=B+'project/components/%s/'%n; os.makedirs(d,exist_ok=True); open(d+'preview.html','w').write(s)
    assert len(s.encode())<256*1024
print(len(P),'previews')

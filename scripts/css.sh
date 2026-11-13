#!/bin/sh
# usage: css.sh Comp [grep]
f=$(ls /private/tmp/claude-501/-Users-will-second-brain/56790265-d246-44e6-a02d-a0051c52481d/scratchpad/polaris-ds/src/react/package/build/esnext/components/$1/*.out.css)
cat $f | tr -s ' \n' ' ' | sed 's/}/}\n/g' | sed -E 's/_[a-z0-9]{5}//g; s/Polaris-//g' | grep -vE 'forced-colors|@media print|Pressable' | grep -E "${2:-.}"

#!/bin/bash

case $1 in

"coolicool"|"cool")
#coolicool
curl -X DELETE "https://api.cloudflare.com/client/v4/zones/ac8fffead047ebb06ed34467899404df/purge_cache" \
     -H "X-Auth-Email: domain@aukeys.com" \
     -H "X-Auth-Key: 91a6bfdbd9a9ff44ab332cae545f93750a841" \
     -H "Content-Type: application/json" \
     --data '{"purge_everything":true}'

;;
"efox.com.pt"|"pt")
#efox.com.pt
curl -X DELETE "https://api.cloudflare.com/client/v4/zones/60020b6502c158452a6c57c3f6aedf9d/purge_cache" \
     -H "X-Auth-Email: domain@aukeys.com" \
     -H "X-Auth-Key: 91a6bfdbd9a9ff44ab332cae545f93750a841" \
     -H "Content-Type: application/json" \
     --data '{"purge_everything":true}'
;;
"efox-shop.com"|"efox-shop")
#efox-shop.com
curl -X DELETE "https://api.cloudflare.com/client/v4/zones/7814b4abad2fc0e5c1fadc0870f4f2df/purge_cache" \
     -H "X-Auth-Email: domain@aukeys.com" \
     -H "X-Auth-Key: 91a6bfdbd9a9ff44ab332cae545f93750a841" \
     -H "Content-Type: application/json" \
     --data '{"purge_everything":true}'

;;
"efoxtienda.com"|"efoxtienda")
#efoxtienda.com
curl -X DELETE "https://api.cloudflare.com/client/v4/zones/fef42b67d86a7c5e7ceb99514c251529/purge_cache" \
     -H "X-Auth-Email: domain@aukeys.com" \
     -H "X-Auth-Key: 91a6bfdbd9a9ff44ab332cae545f93750a841" \
     -H "Content-Type: application/json" \
     --data '{"purge_everything":true}'
;;

"firstfun.com"|"firstfun")
#firstfun.com
curl -X DELETE "https://api.cloudflare.com/client/v4/zones/038145436ef4e4b8f351d0154c8c7d4a/purge_cache" \
     -H "X-Auth-Email: domain@aukeys.com" \
     -H "X-Auth-Key: 91a6bfdbd9a9ff44ab332cae545f93750a841" \
     -H "Content-Type: application/json" \
     --data '{"purge_everything":true}'
;;
"foxcute.com"|"foxcute")
#foxcute.com
curl -X DELETE "https://api.cloudflare.com/client/v4/zones/37a1ceaa7cbc20e0cf12a90eb1abfff4/purge_cache" \
     -H "X-Auth-Email: domain@aukeys.com" \
     -H "X-Auth-Key: 91a6bfdbd9a9ff44ab332cae545f93750a841" \
     -H "Content-Type: application/json" \
     --data '{"purge_everything":true}'
;;
"myefox.fr"|"fr")
#myefox.fr
curl -X DELETE "https://api.cloudflare.com/client/v4/zones/466d26fb11905454bebe8abf557d6969/purge_cache" \
     -H "X-Auth-Email: domain@aukeys.com" \
     -H "X-Auth-Key: 91a6bfdbd9a9ff44ab332cae545f93750a841" \
     -H "Content-Type: application/json" \
     --data '{"purge_everything":true}'

;;
"myefox.it"|"it")
#myefox.it
curl -X DELETE "https://api.cloudflare.com/client/v4/zones/3de6644e4f178b6846a4abe6997733e9/purge_cache" \
     -H "X-Auth-Email: domain@aukeys.com" \
     -H "X-Auth-Key: 91a6bfdbd9a9ff44ab332cae545f93750a841" \
     -H "Content-Type: application/json" \
     --data '{"purge_everything":true}'
;;
"tabouf.com"|"tabouf")
#tabouf.com 
curl -X DELETE "https://api.cloudflare.com/client/v4/zones/54cef4b7e0c3c832d9c9833da12b7be0/purge_cache" \
     -H "X-Auth-Email: domain@aukeys.com" \
     -H "X-Auth-Key: 91a6bfdbd9a9ff44ab332cae545f93750a841" \
     -H "Content-Type: application/json" \
     --data '{"purge_everything":true}'
;;
*)
echo
echo  "Clear cloudflare cache web,css,html,image"
echo -n "\033[31;1m Pleae input :\n\tcool/coolicool\n\tpt/efox.com.pt\n\tefox-shop/efox-shop.com\n\tefoxtienda/efoxtienda.com\n\tfirstfun/firstfun.com\n\tfoxcute/foxcute.com\n\tfr/myefox.fr\n\tit/myefox.it\n\ttabouf/tabouf.com\033[0m"
echo
esac


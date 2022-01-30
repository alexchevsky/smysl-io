/*!
 * Likely 2.6.0 by Ilya Birman (ilyabirman.net), Nikolay Rys (linkedin.com/in/nikolay-rys), 
 * Viktor Karpov (https://twitter.com/vitkarpov), and contributors.
 * Special thanks to Ivan Akulov (iamakulov.com) and Evgeny Steblinsky (volter9.github.io).
 * Inspired by Social Likes by Artem Sapegin (sapegin.me).
 */
!function(t,e){"object"==typeof exports&&"object"==typeof module?module.exports=e():"function"==typeof define&&define.amd?define([],e):"object"==typeof exports?exports.likely=e():t.likely=e()}(this,function(){return function(t){function e(r){if(n[r])return n[r].exports;var i=n[r]={i:r,l:!1,exports:{}};return t[r].call(i.exports,i,i.exports,e),i.l=!0,i.exports}var n={};return e.m=t,e.c=n,e.i=function(t){return t},e.d=function(t,n,r){e.o(t,n)||Object.defineProperty(t,n,{configurable:!1,enumerable:!0,get:r})},e.n=function(t){var n=t&&t.__esModule?function(){return t.default}:function(){return t};return e.d(n,"a",n),n},e.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},e.p="",e(e.s=22)}([function(t,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0}),function(t){function r(t,e,n){return e in t?Object.defineProperty(t,e,{value:n,enumerable:!0,configurable:!0,writable:!0}):t[e]=n,t}n.d(e,"toArray",function(){return a}),n.d(e,"mergeToNew",function(){return c}),n.d(e,"extendWith",function(){return u}),n.d(e,"getDataset",function(){return s}),n.d(e,"getBools",function(){return l}),n.d(e,"interpolateStr",function(){return p}),n.d(e,"interpolateUrl",function(){return d}),n.d(e,"joinIntoParams",function(){return f}),n.d(e,"registerGlobalCallback",function(){return C}),n.d(e,"getDefaultUrl",function(){return h}),n.d(e,"isBrowserEnv",function(){return v}),n.d(e,"renameKey",function(){return y});var i="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(t){return typeof t}:function(t){return t&&"function"==typeof Symbol&&t.constructor===Symbol&&t!==Symbol.prototype?"symbol":typeof t},o={yes:!0,no:!1};Object.entries||(Object.entries=function(t){for(var e=Object.keys(t),n=e.length,r=new Array(n);n--;)r[n]=[e[n],t[e[n]]];return r});var a=function(t){return Array.prototype.slice.call(t)},c=function(){for(var t={},e=Array.prototype.slice.call(arguments),n=0;n<e.length;n++){var r=e[n];if(r)for(var i in r)Object.prototype.hasOwnProperty.call(r,i)&&(t[i]=r[i])}return t},u=function(t,e){for(var n in e)Object.prototype.hasOwnProperty.call(e,n)&&(t[n]=e[n]);return t},s=function(t){if("object"===i(t.dataset))return t.dataset;var e=void 0,n={},r=t.attributes,o=void 0,a=void 0,c=function(t){return t.charAt(1).toUpperCase()};for(e=r.length-1;e>=0;e--)(o=r[e])&&o.name&&/^data-\w[\w-]*$/.test(o.name)&&(a=o.name.substr(5).replace(/-./g,c),n[a]=o.value);return n},l=function(t){var e={},n=s(t);for(var r in n)if(Object.prototype.hasOwnProperty.call(n,r)){var i=n[r];e[r]=i in o?o[i]:i}return e},p=function(t,e){return t?t.replace(/\{([^}]+)\}/g,function(t,n){return n in e?e[n]:t}):""},d=function(t,e){for(var n in e)Object.prototype.hasOwnProperty.call(e,n)&&(e[n]=encodeURIComponent(e[n]));return p(t,e)},f=function(t){var e=encodeURIComponent,n=[];for(var r in t)"object"!==i(t[r])&&n.push(e(r)+"="+e(t[r]));return n.join("&")},C=function(e,n){var r=e.split("."),i=null,o=t;r.forEach(function(t,e){void 0===o[t]&&(o[t]={}),e!==r.length-1&&(o=o[t]),i=t}),o[i]=n},h=function(){var t=document.querySelector('link[rel="canonical"]');return t?t.href:window.location.href.replace(window.location.hash,"")},v="undefined"!=typeof window&&"undefined"!=typeof document&&document.createElement,y=function(t,e,n){Object.prototype.hasOwnProperty.call(t,e)&&delete Object.assign(t,r({},n,t[e]))[e]}}.call(e,n(21))},function(t,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0}),n.d(e,"global",function(){return o}),n.d(e,"wrapSVG",function(){return c}),n.d(e,"createNode",function(){return u}),n.d(e,"loadJSONP",function(){return s}),n.d(e,"find",function(){return l}),n.d(e,"findAll",function(){return p}),n.d(e,"openPopup",function(){return d}),n.d(e,"createTempLink",function(){return f});var r=n(0),i={},o=r.isBrowserEnv?window:i,a=r.isBrowserEnv?document.createElement("div"):{},c=function(t){return'<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16"><path d="M'+t+'z"/></svg>'},u=function(t){return a.innerHTML=t,a.children[0]},s=function(t){var e=document.createElement("script"),n=document.head;e.type="text/javascript",e.src=t,n.appendChild(e),n.removeChild(e)},l=function(t,e){return(e||document).querySelector(t)},p=function(t,e){return Array.prototype.slice.call((e||document).querySelectorAll(t))},d=function(t,e,n,r){var i=Math.round(screen.width/2-n/2),o=0;screen.height>r&&(o=Math.round(screen.height/3-r/2));var a="left="+i+",top="+o+",width="+n+",height="+r+",personalbar=0,toolbar=0,scrollbars=1,resizable=1",c=window.open(t,e,a);return c?(c.focus(),c):(location.href=t,null)},f=function(t){var e=document.createElement("a");e.href=t,e.style="display: none",document.body.appendChild(e),setTimeout(function(){e.click(),document.body.removeChild(e)})}},function(t,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0}),e.default={name:"likely",prefix:"likely__"}},function(t,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var r=n(8),i=n(9),o=n(10),a=n(11),c=n(12),u=n(13),s=n(14),l=n(15),p=n(16),d=n(17),f=n(18),C=function(){function t(t,e){var n=[],r=!0,i=!1,o=void 0;try{for(var a,c=t[Symbol.iterator]();!(r=(a=c.next()).done)&&(n.push(a.value),!e||n.length!==e);r=!0);}catch(t){i=!0,o=t}finally{try{!r&&c.return&&c.return()}finally{if(i)throw o}}return n}return function(e,n){if(Array.isArray(e))return e;if(Symbol.iterator in Object(e))return t(e,n);throw new TypeError("Invalid attempt to destructure non-iterable instance")}}(),h={facebook:i.a,linkedin:o.a,odnoklassniki:a.a,pinterest:c.a,reddit:u.a,telegram:s.a,twitter:l.a,viber:p.a,vkontakte:d.a,whatsapp:f.a};Object.entries(h).forEach(function(t){var e=C(t,2),i=e[0],o=e[1];n.i(r.a)(o),o.name=i}),e.default=h},function(t,e,n){var r=n(0),i=r.getBools,o=r.getDefaultUrl,a=r.mergeToNew,c=n(19).default,u=n(2).default,s=n(1),l=s.findAll,p=n(7).default,d=n(3).default;n(20);var f=function(t,e){var n=e||{},r={counters:!0,timeout:1e3,zeroes:!1,title:document.title,url:o()},s=a(r,n,i(t)),l=t[u.name];return l?l.update(s):t[u.name]=new c(t,s),l},C={initiate:function(t,e){function n(){r.forEach(function(t){f(t,i)})}var r=void 0,i=void 0;Array.isArray(t)?(r=t,i=e):t instanceof Node?(r=[t],i=e):(r=l("."+u.name),i=t),this.maintainStoredData(i),n(),p.onUrlChange(n)},maintainStoredData:function(t){t&&t.forceUpdate&&Object.keys(d).forEach(function(t){d[t].resetBroadcasters()})},deprecationsShown:!1};t.exports=C},function(t,e,n){"use strict";function r(t,e){if(!(t instanceof e))throw new TypeError("Cannot call a class as a function")}var i=n(1),o=n(0),a=n(2),c=n(6),u=n(3),s=function(){function t(t,e){for(var n=0;n<e.length;n++){var r=e[n];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(t,r.key,r)}}return function(e,n,r){return n&&t(e.prototype,n),r&&t(e,r),e}}(),l='<span class="{className}">{content}</span>',p=function(){function t(e,i,a){r(this,t),this.widget=e,this.likely=i,this.options=n.i(o.mergeToNew)(a),this.detectService(),this.isConnected()&&this.detectParams()}return s(t,[{key:"isConnected",value:function(){return void 0!==this.options.service}},{key:"isUnrecognized",value:function(){return!this.isConnected()&&!this.options.foreign}},{key:"prepare",value:function(){this.isConnected()&&(this.initHtml(),this.registerAsCounted())}},{key:"update",value:function(t){var e="."+a.default.prefix+"counter",r=n.i(i.findAll)(e,this.widget);n.i(o.extendWith)(this.options,n.i(o.mergeToNew)({forceUpdate:!1},t)),r.forEach(function(t){t.parentNode.removeChild(t)}),this.registerAsCounted()}},{key:"detectService",value:function(){var t=n.i(o.toArray)(this.widget.classList),e=t.filter(function(t){return Object.prototype.hasOwnProperty.call(u.default,t)})[0];e?this.options.service=u.default[e]:t.includes("likely__widget")&&(this.options.foreign=!0)}},{key:"detectParams",value:function(){var t=this.options;this.data=n.i(o.getDataset)(this.widget);var e=[];for(var r in this.data)-1===this.options.service.knownParams.indexOf(r)&&e.push(r);if(e.length>0){var i=e.join(", ");console.warn("LIKELY DEPRECATION: unsupported parameters “%s” on “%s” button. They will be ignored in version 3.0.",i,this.options.service.name)}this.data.counter&&(t.staticCounter=this.data.counter),t.url=void 0===this.data.url?t.url:this.data.url,t.title=void 0===this.data.title?t.title:this.data.title,delete this.data.counter,delete this.data.url,delete this.data.title}},{key:"initHtml",value:function(){var t=this.options,e=this.widget,r=e.innerHTML;e.addEventListener("click",this.click.bind(this)),e.classList.remove(this.options.service.name),e.className+=""+this.className("widget");var a=n.i(o.interpolateStr)(l,{className:this.className("button"),content:r}),c=n.i(o.interpolateStr)(l,{className:this.className("icon"),content:n.i(i.wrapSVG)(t.service.svgIconPath)});e.innerHTML=c+a}},{key:"registerAsCounted",value:function(){var t=this.options;t.counters&&t.service.counterUrl&&(t.staticCounter?this.setDisplayedCounter(t.staticCounter):n.i(c.a)(this.setDisplayedCounter.bind(this),t))}},{key:"className",value:function(t){var e=a.default.prefix+t;return e+" "+e+"_"+this.options.service.name}},{key:"setDisplayedCounter",value:function(t){var e=parseInt(t,10)||0,r=n.i(i.find)("."+a.default.name+"__counter",this.widget);r&&r.parentNode.removeChild(r);var c={className:this.className("counter"),content:e};e||this.options.zeroes||(c.className+=" "+a.default.prefix+"counter_empty",c.content=""),this.widget.appendChild(n.i(i.createNode)(n.i(o.interpolateStr)(l,c))),this.likely.finalize()}},{key:"click",value:function(){var t=this.options;if(t.service.clickCallback.call(this)){var e=n.i(o.interpolateUrl)(t.service.popupUrl,{url:t.url,title:t.title,content:t.content}),r=this.addAdditionalParamsToUrl(e);if(!1===t.service.openPopup)return n.i(i.createTempLink)(r),!1;n.i(i.openPopup)(r,a.default.prefix+this.options.service.name,t.service.popupWidth,t.service.popupHeight)}return!1}},{key:"addAdditionalParamsToUrl",value:function(t){var e=n.i(o.joinIntoParams)(this.data),r=-1===t.indexOf("?")?"?":"&";return""===e?t:t+r+e}}]),t}();e.a=p},function(t,e,n){"use strict";function r(t,e){this.url=n.i(i.interpolateUrl)(t,{url:e}),this.setters=[],this.value=void 0}var i=n(0);r.prototype.register=function(t){this.setters.push(t),this.value&&t(this.value)},r.prototype.trigger=function(t){this.value=t,this.setters.forEach(function(e){e(t)})},e.a=function(t,e){var n=e.service.broadcastersByUrl[e.url];n||(n=new r(e.service.counterUrl,e.url),e.service.broadcastersByUrl[e.url]=n,e.service.fetch(n)),n.register(t)}},function(t,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var r=[],i=function(){r.forEach(function(t){t()})},o=function(){var t=window.history.pushState;window.history.pushState=function(){return setTimeout(i,0),t.apply(window.history,arguments)};var e=window.history.replaceState;window.history.replaceState=function(){return setTimeout(i,0),e.apply(window.history,arguments)},window.addEventListener("popstate",i)},a=!1,c={onUrlChange:function(t){a||(o(),a=!0),r.push(t)}};e.default=c},function(t,e,n){"use strict";function r(t){var e=this,n=new XMLHttpRequest;n.onreadystatechange=function(){if(4===n.readyState&&200===n.status){var r="function"==typeof e.convertNumber?e.convertNumber(n.responseText):n.responseText;t.trigger(r)}},n.open("GET",t.url,!0),n.send()}function i(){this.broadcastersByUrl={}}var o=n(1);e.a=function(t){t.fetch=o.global.__likelyFetchMock||t.fetch||r,t.clickCallback=t.clickCallback||function(){return!0},t.knownParams=t.knownParams||[],t.resetBroadcasters=i,t.resetBroadcasters()}},function(t,e,n){"use strict";e.a={counterUrl:"https://graph.facebook.com/?id={url}&access_token=1729830587180291|102e6d79cda2fa63b65c99c039eed12a&fields=og_object%7Bengagement%7Bcount%7D%7D",convertNumber:function(t){var e=JSON.parse(t).og_object;return e?e.engagement.count:0},popupWidth:555,popupHeight:555,popupUrl:"https://www.facebook.com/sharer.php?u={url}",knownParams:["url","quote","hashtag","counter"],svgIconPath:"16.000,8.049 C16.000,3.629 12.418,0.047 8.000,0.047 C3.582,0.047 -0.000,3.629 -0.000,8.049 C-0.000,12.043 2.925,15.353 6.750,15.953 L6.750,10.362 L4.719,10.362 L4.719,8.049 L6.750,8.049 L6.750,6.286 C6.750,4.280 7.944,3.173 9.772,3.173 C10.647,3.173 11.563,3.329 11.563,3.329 L11.563,5.298 L10.554,5.298 C9.560,5.298 9.250,5.915 9.250,6.548 L9.250,8.049 L11.469,8.049 L11.114,10.362 L9.250,10.362 L9.250,15.953 C13.075,15.353 16.000,12.043 16.000,8.049"}},function(t,e,n){"use strict";e.a={popupUrl:"https://www.linkedin.com/sharing/share-offsite/?url={url}",knownParams:["url"],popupWidth:600,popupHeight:500,svgIconPath:"13.634,13.629 L11.263,13.629 L11.263,9.919 C11.263,9.035 11.247,7.896 10.030,7.896 C8.795,7.896 8.606,8.860 8.606,9.855 L8.606,13.629 L6.234,13.629 L6.234,6.000 L8.510,6.000 L8.510,7.043 L8.542,7.043 C9.006,6.250 9.869,5.777 10.788,5.811 C13.191,5.811 13.634,7.392 13.634,9.445 L13.634,13.629 ZM3.560,4.958 C2.800,4.958 2.184,4.343 2.184,3.583 C2.183,2.824 2.799,2.209 3.559,2.208 C4.319,2.208 4.935,2.823 4.935,3.583 L4.935,3.583 C4.936,4.342 4.320,4.957 3.560,4.958 M4.746,13.629 L2.372,13.629 L2.372,6.000 L4.745,6.000 L4.746,13.629 ZM14.816,0.007 L1.181,0.007 C0.536,0.000 0.008,0.516 -0.000,1.160 L-0.000,14.839 C0.007,15.484 0.536,16.000 1.181,15.993 L14.816,15.993 C15.461,16.000 15.991,15.484 16.000,14.839 L16.000,1.160 C15.991,0.515 15.461,-0.000 14.816,0.007"}},function(t,e,n){"use strict";var r=n(0);e.a={counterUrl:"https://connect.ok.ru/dk?st.cmd=extLike&tp=json&ref={url}",convertNumber:function(t){return JSON.parse(t).count},clickCallback:function(){return n.i(r.renameKey)(this.widget.dataset,"imageurl","imageUrl"),!0},popupWidth:588,popupHeight:296,popupUrl:"https://connect.ok.ru/offer?url={url}&title={title}",knownParams:["url","title","imageurl","counter"],svgIconPath:"12.1,10.6c-0.7,0.5-1.5,0.8-2.4,1l2.3,2.3c0.5,0.5,0.5,1.2,0,1.7c-0.5,0.5-1.2,0.5-1.7,0L8,13.4l-2.3,2.3 C5.5,15.9,5.2,16,4.9,16c-0.3,0-0.6-0.1-0.9-0.4c-0.5-0.5-0.5-1.2,0-1.7l2.3-2.3c-0.8-0.2-1.7-0.5-2.4-1C3.4,10.3,3.2,9.6,3.5,9 c0.4-0.6,1.1-0.7,1.7-0.4c1.7,1.1,3.9,1.1,5.6,0c0.6-0.4,1.3-0.2,1.7,0.4C12.8,9.5,12.6,10.3,12.1,10.6z M8,8.3 c-2.3,0-4.1-1.9-4.1-4.1C3.9,1.8,5.7,0,8,0c2.3,0,4.1,1.9,4.1,4.1C12.1,6.4,10.3,8.3,8,8.3z M8,2.4c-1,0-1.7,0.8-1.7,1.7 c0,0.9,0.8,1.7,1.7,1.7c0.9,0,1.7-0.8,1.7-1.7C9.7,3.2,9,2.4,8,2.4"}},function(t,e,n){"use strict";e.a={counterUrl:"https://api.pinterest.com/v1/urls/count.json?url={url}&callback=jsonp",convertNumber:function(t){var e=t.slice(6,t.length-1);return JSON.parse(e).count},popupUrl:"https://pinterest.com/pin/create/button/?url={url}&description={title}",popupWidth:750,popupHeight:750,knownParams:["url","title","media","counter"],svgIconPath:"7.99 0c-4.417 0-8 3.582-8 8 0 3.39 2.11 6.284 5.086 7.45-.07-.633-.133-1.604.028-2.295.145-.624.938-3.977.938-3.977s-.24-.48-.24-1.188c0-1.112.645-1.943 1.448-1.943.683 0 1.012.512 1.012 1.127 0 .686-.437 1.713-.663 2.664-.19.796.398 1.446 1.184 1.446 1.422 0 2.515-1.5 2.515-3.664 0-1.915-1.377-3.255-3.343-3.255-2.276 0-3.612 1.707-3.612 3.472 0 .688.265 1.425.595 1.826.065.08.075.15.055.23-.06.252-.195.796-.222.907-.035.146-.116.177-.268.107-1-.465-1.624-1.926-1.624-3.1 0-2.523 1.835-4.84 5.287-4.84 2.775 0 4.932 1.977 4.932 4.62 0 2.757-1.74 4.976-4.152 4.976-.81 0-1.573-.42-1.834-.92l-.498 1.903c-.18.695-.668 1.566-.994 2.097.75.232 1.544.357 2.37.357 4.417 0 8-3.582 8-8s-3.583-8-8-8"}},function(t,e,n){"use strict";e.a={counterUrl:"https://www.reddit.com/search.json?q=url:{url}&sort=top&type=link&limit=5",convertNumber:function(t){var e=JSON.parse(t),n=0;return e.data.children.forEach(function(t){t.data&&t.data.score&&(n+=t.data.score)}),n},popupUrl:"https://reddit.com/submit?url={url}&title={title}",popupWidth:785,popupHeight:550,knownParams:["url","title","counter"],svgIconPath:"15.936 8.186 C 15.936 7.227 15.159 6.45 14.2 6.45 C 13.732 6.45 13.308 6.636 12.995 6.937 C 11.808 6.08 10.173 5.527 8.352 5.464 L 9.143 1.742 L 11.727 2.291 C 11.758 2.949 12.296 3.473 12.961 3.473 C 13.646 3.473 14.202 2.918 14.202 2.233 C 14.202 1.548 13.646 0.992 12.961 0.992 C 12.474 0.992 12.057 1.276 11.854 1.685 L 8.968 1.071 C 8.888 1.054 8.804 1.069 8.735 1.114 C 8.666 1.159 8.617 1.23 8.6 1.31 L 7.717 5.462 C 5.869 5.514 4.207 6.068 3.005 6.934 C 2.693 6.634 2.271 6.45 1.804 6.45 C 0.845 6.45 0.068 7.227 0.068 8.186 C 0.068 8.892 0.489 9.498 1.094 9.769 C 1.067 9.942 1.052 10.117 1.052 10.295 C 1.052 12.966 4.162 15.132 7.998 15.132 C 11.834 15.132 14.944 12.966 14.944 10.295 C 14.944 10.118 14.929 9.944 14.903 9.773 C 15.511 9.503 15.936 8.894 15.936 8.186 Z M 4.031 9.427 C 4.031 8.743 4.588 8.186 5.272 8.186 C 5.955 8.186 6.512 8.743 6.512 9.427 C 6.512 10.11 5.955 10.667 5.272 10.667 C 4.588 10.667 4.031 10.11 4.031 9.427 Z M 10.947 12.704 C 10.101 13.549 8.478 13.615 8.001 13.615 C 7.524 13.615 5.902 13.549 5.057 12.704 C 4.931 12.578 4.931 12.375 5.057 12.249 C 5.182 12.124 5.386 12.124 5.511 12.249 C 6.045 12.783 7.186 12.972 8.001 12.972 C 8.817 12.972 9.958 12.783 10.493 12.249 C 10.619 12.124 10.822 12.124 10.947 12.249 C 11.073 12.375 11.073 12.578 10.947 12.704 Z M 10.729 10.667 C 10.045 10.667 9.488 10.11 9.488 9.427 C 9.488 8.743 10.045 8.186 10.729 8.186 C 11.413 8.186 11.969 8.743 11.969 9.427 C 11.969 10.11 11.413 10.667 10.729 10.667"}},function(t,e,n){"use strict";e.a={popupUrl:"https://telegram.me/share/url?url={url}&text={title}",popupWidth:485,popupHeight:355,knownParams:["url","title"],svgIconPath:"1.155 7.049 C 5.43 5.188 8.281 3.962 9.708 3.369 C 13.781 1.677 14.627 1.384 15.179 1.374 C 15.3 1.372 15.571 1.402 15.747 1.544 C 15.895 1.664 15.936 1.827 15.956 1.941 C 15.975 2.055 15.999 2.314 15.98 2.517 C 15.759 4.834 14.804 10.454 14.319 13.048 C 14.113 14.146 13.708 14.514 13.316 14.55 C 12.465 14.628 11.818 13.988 10.993 13.448 C 9.702 12.603 8.973 12.077 7.72 11.252 C 6.272 10.299 7.211 9.775 8.036 8.919 C 8.252 8.695 12.004 5.286 12.077 4.977 C 12.086 4.938 12.095 4.794 12.009 4.718 C 11.923 4.642 11.797 4.668 11.705 4.689 C 11.576 4.718 9.514 6.079 5.519 8.772 C 4.934 9.174 4.404 9.369 3.929 9.359 C 3.405 9.348 2.398 9.063 1.649 8.82 C 0.731 8.522 0.001 8.364 0.064 7.858 C 0.097 7.594 0.461 7.325 1.155 7.049"}},function(t,e,n){"use strict";e.a={popupUrl:"https://twitter.com/intent/tweet?url={url}&text={title}",popupWidth:600,popupHeight:450,clickCallback:function(){return/[.?:\-–—]\s*$/.test(this.options.title)||(this.options.title+=":"),!0},knownParams:["url","title","via","hashtags"],svgIconPath:"15.969,3.058c-0.586,0.26-1.217,0.436-1.878,0.515c0.675-0.405,1.194-1.045,1.438-1.809c-0.632,0.375-1.332,0.647-2.076,0.793c-0.596-0.636-1.446-1.033-2.387-1.033c-1.806,0-3.27,1.464-3.27,3.27 c0,0.256,0.029,0.506,0.085,0.745C5.163,5.404,2.753,4.102,1.14,2.124C0.859,2.607,0.698,3.168,0.698,3.767 c0,1.134,0.577,2.135,1.455,2.722C1.616,6.472,1.112,6.325,0.671,6.08c0,0.014,0,0.027,0,0.041c0,1.584,1.127,2.906,2.623,3.206 C3.02,9.402,2.731,9.442,2.433,9.442c-0.211,0-0.416-0.021-0.615-0.059c0.416,1.299,1.624,2.245,3.055,2.271 c-1.119,0.877-2.529,1.4-4.061,1.4c-0.264,0-0.524-0.015-0.78-0.046c1.447,0.928,3.166,1.469,5.013,1.469 c6.015,0,9.304-4.983,9.304-9.304c0-0.142-0.003-0.283-0.009-0.423C14.976,4.29,15.531,3.714,15.969,3.058"}},function(t,e,n){"use strict";e.a={popupUrl:"viber://forward?text={content}",clickCallback:function(){return this.options.title?this.options.content=this.options.title+"\n"+this.options.url:this.options.content=this.options.url,!0},openPopup:!1,knownParams:["url","title"],svgIconPath:"5.24 12.7 C 5.24 12.7 5.24 13.21 5.24 13.21 C 5.24 13.21 5.21 13.61 5.21 13.61 C 5.21 13.61 5.21 15.65 5.21 15.65 C 5.21 15.65 5.21 15.81 5.21 15.81 C 5.24 15.98 5.36 16.05 5.5 15.95 C 5.63 15.87 5.91 15.54 6.02 15.41 C 6.02 15.41 7.34 13.83 7.34 13.83 C 7.34 13.83 7.74 13.35 7.74 13.35 C 7.78 13.29 7.86 13.17 7.93 13.16 C 7.93 13.16 8.27 13.16 8.27 13.16 C 8.27 13.16 9.55 13.16 9.55 13.16 C 9.55 13.16 9.84 13.13 9.84 13.13 C 10.69 13.1 11.54 12.97 12.37 12.75 C 13.36 12.49 14.01 12.3 14.74 11.5 C 15.42 10.75 15.71 9.75 15.85 8.76 C 15.85 8.76 15.95 7.64 15.95 7.64 C 15.95 7.64 15.97 7.37 15.97 7.37 C 15.97 7.37 16 6.78 16 6.78 C 16 6.78 16 6.08 16 6.08 C 16 6.08 15.97 5.57 15.97 5.57 C 15.97 5.57 15.95 5.31 15.95 5.31 C 15.92 4.88 15.86 4.47 15.78 4.05 C 15.59 3.05 15.22 2.1 14.49 1.4 C 14.18 1.1 13.65 0.86 13.26 0.7 C 12.59 0.43 11.85 0.26 11.14 0.16 C 11.14 0.16 10.18 0.05 10.18 0.05 C 10.18 0.05 9.68 0.03 9.68 0.03 C 9.68 0.03 9.16 0.03 9.16 0.03 C 9.16 0.03 8.82 0 8.82 0 C 8.82 0 8.24 0.03 8.24 0.03 C 8.24 0.03 7.98 0.03 7.98 0.03 C 7.98 0.03 7.72 0.05 7.72 0.05 C 6.73 0.12 5.75 0.29 4.82 0.67 C 4.35 0.86 3.77 1.19 3.41 1.55 C 2.51 2.48 2.2 3.83 2.07 5.09 C 2.07 5.09 2.03 5.71 2.03 5.71 C 2.03 5.71 2.03 6.16 2.03 6.16 C 2.03 6.16 2 6.57 2 6.57 C 2 6.57 2 7.45 2 7.45 C 2 7.45 2.03 7.99 2.03 7.99 C 2.03 7.99 2.1 8.74 2.1 8.74 C 2.25 9.81 2.6 10.87 3.36 11.65 C 3.59 11.89 3.89 12.11 4.17 12.27 C 4.43 12.43 4.94 12.66 5.24 12.7 Z M 8.82 1.94 C 9.21 1.88 9.98 2.02 10.36 2.15 C 11.72 2.62 12.71 3.58 13.17 4.98 C 13.35 5.53 13.41 6.11 13.44 6.67 C 13.46 7.04 13.16 7.08 13.03 6.94 C 12.95 6.84 12.97 6.71 12.97 6.59 C 12.97 6.59 12.95 6.32 12.95 6.32 C 12.89 5.58 12.69 4.84 12.29 4.21 C 11.7 3.29 10.73 2.66 9.68 2.47 C 9.68 2.47 9.18 2.41 9.18 2.41 C 9.06 2.41 8.85 2.42 8.74 2.34 C 8.62 2.24 8.63 2.02 8.82 1.94 Z M 5.79 2.45 C 6.24 2.4 6.34 2.6 6.6 2.92 C 6.9 3.29 7.09 3.56 7.34 3.97 C 7.46 4.17 7.59 4.38 7.61 4.64 C 7.62 4.72 7.6 4.8 7.58 4.88 C 7.43 5.4 6.92 5.37 6.81 5.84 C 6.75 6.1 6.99 6.58 7.12 6.81 C 7.55 7.61 8.19 8.35 9.03 8.72 C 9.23 8.81 9.6 8.99 9.81 8.94 C 10.15 8.86 10.25 8.54 10.47 8.31 C 10.6 8.18 10.75 8.13 10.93 8.12 C 11.25 8.11 11.38 8.23 11.64 8.39 C 12.05 8.65 12.36 8.89 12.74 9.2 C 12.95 9.38 13.17 9.58 13.14 9.89 C 13.12 10.16 12.94 10.43 12.78 10.64 C 12.65 10.8 12.48 11 12.32 11.13 C 12.11 11.29 11.87 11.41 11.61 11.44 C 11.45 11.45 11.24 11.37 11.09 11.32 C 10.72 11.19 10.29 10.97 9.94 10.79 C 8.96 10.29 8.03 9.67 7.22 8.9 C 7.22 8.9 7.02 8.71 7.02 8.71 C 6.15 7.79 5.5 6.74 4.95 5.6 C 4.78 5.26 4.61 4.92 4.49 4.56 C 4.43 4.38 4.38 4.29 4.38 4.1 C 4.37 3.78 4.5 3.49 4.7 3.24 C 4.82 3.09 5.01 2.92 5.16 2.8 C 5.36 2.64 5.54 2.5 5.79 2.45 Z M 9.18 3.12 C 9.44 3.07 9.9 3.18 10.15 3.25 C 11.1 3.53 11.8 4.21 12.12 5.17 C 12.19 5.39 12.26 5.72 12.26 5.95 C 12.27 6.05 12.28 6.36 12.25 6.43 C 12.2 6.54 12.06 6.59 11.95 6.53 C 11.79 6.45 11.83 6.27 11.82 6.11 C 11.82 6.11 11.79 5.9 11.79 5.9 C 11.76 5.47 11.61 5.04 11.37 4.69 C 11.03 4.2 10.53 3.85 9.97 3.7 C 9.97 3.7 9.52 3.6 9.52 3.6 C 9.45 3.59 9.24 3.57 9.18 3.54 C 9.02 3.47 9 3.23 9.18 3.12 Z M 9.55 4.33 C 9.69 4.3 9.8 4.32 9.94 4.35 C 10.45 4.45 10.84 4.75 11.02 5.25 C 11.09 5.44 11.15 5.73 11.14 5.92 C 11.13 6.08 11.04 6.18 10.88 6.16 C 10.76 6.14 10.72 6.06 10.69 5.95 C 10.63 5.68 10.68 5.56 10.52 5.28 C 10.38 5.04 10.15 4.88 9.89 4.82 C 9.71 4.79 9.43 4.81 9.38 4.58 C 9.36 4.45 9.44 4.37 9.55 4.33"}},function(t,e,n){"use strict";var r=n(0),i=n(1),o={popupWidth:650,popupHeight:570,counterUrl:"https://vk.com/share.php?act=count&url={url}&index={index}",fetch:function(t){var e=Object.keys(this.broadcastersByUrl).length-1;n.i(i.loadJSONP)(n.i(r.interpolateUrl)(t.url,{index:e}))},popupUrl:"https://vk.com/share.php?url={url}&title={title}",knownParams:["url","title","image","comment","counter"],svgIconPath:"15.632 3.914 C 15.743 3.545 15.632 3.273 15.102 3.273 L 13.351 3.273 C 12.906 3.273 12.701 3.508 12.59 3.766 C 12.59 3.766 11.699 5.926 10.438 7.329 C 10.03 7.736 9.845 7.865 9.622 7.865 C 9.511 7.865 9.35 7.736 9.35 7.367 L 9.35 3.914 C 9.35 3.471 9.221 3.273 8.85 3.273 L 6.099 3.273 C 5.82 3.273 5.653 3.479 5.653 3.674 C 5.653 4.094 6.284 4.191 6.349 5.373 L 6.349 7.939 C 6.349 8.501 6.247 8.604 6.024 8.604 C 5.431 8.604 3.987 6.434 3.131 3.951 C 2.963 3.468 2.795 3.273 2.347 3.273 L 0.597 3.273 C 0.096 3.273 -0.004 3.508 -0.004 3.766 C -0.004 4.228 0.59 6.517 2.76 9.545 C 4.206 11.613 6.245 12.734 8.099 12.734 C 9.212 12.734 9.35 12.484 9.35 12.056 L 9.35 10.493 C 9.35 9.995 9.455 9.896 9.808 9.896 C 10.067 9.896 10.513 10.025 11.551 11.022 C 12.738 12.203 12.934 12.734 13.602 12.734 L 15.352 12.734 C 15.852 12.734 16.103 12.484 15.958 11.993 C 15.8 11.504 15.234 10.793 14.482 9.951 C 14.074 9.471 13.461 8.954 13.276 8.696 C 13.016 8.363 13.091 8.216 13.276 7.92 C 13.276 7.92 15.409 4.929 15.632 3.914"};n.i(r.registerGlobalCallback)("VK.Share.count",function(t,e){var n=o.broadcastersByUrl;n[Object.keys(n)[t]].trigger(e)}),e.a=o},function(t,e,n){"use strict";e.a={popupUrl:"whatsapp://send?text={title}%0D%0A%0D%0A{url}",openPopup:!1,knownParams:["url","title"],svgIconPath:"8.013,15.949 L8.009,15.949 C6.574,15.948 5.167,15.564 3.939,14.839 L3.647,14.666 L0.620,15.457 L1.428,12.517 L1.238,12.216 C0.438,10.947 0.015,9.481 0.016,7.976 C0.017,3.584 3.605,0.010 8.016,0.010 C10.152,0.011 12.160,0.841 13.669,2.347 C15.179,3.852 16.010,5.854 16.009,7.983 C16.008,12.375 12.420,15.949 8.013,15.949 ZM12.860,10.262 C12.800,10.162 12.639,10.103 12.399,9.983 C12.159,9.863 10.977,9.283 10.756,9.203 C10.536,9.124 10.376,9.084 10.215,9.323 C10.055,9.563 9.594,10.103 9.454,10.262 C9.314,10.422 9.174,10.442 8.933,10.322 C8.693,10.202 7.918,9.950 7.000,9.134 C6.285,8.499 5.803,7.714 5.663,7.475 C5.522,7.235 5.648,7.105 5.768,6.986 C5.876,6.878 6.008,6.706 6.129,6.566 C6.249,6.426 6.289,6.327 6.369,6.167 C6.449,6.007 6.409,5.867 6.349,5.747 C6.289,5.627 5.822,4.443 5.608,3.969 C5.428,3.570 5.238,3.562 5.067,3.555 C4.927,3.549 4.766,3.549 4.606,3.549 C4.446,3.549 4.185,3.609 3.965,3.849 C3.745,4.089 3.124,4.668 3.124,5.847 C3.124,7.026 3.985,8.165 4.105,8.324 C4.226,8.484 5.769,10.980 8.212,11.941 C10.243,12.739 10.656,12.580 11.097,12.540 C11.538,12.500 12.519,11.961 12.720,11.401 C12.920,10.842 12.920,10.362 12.860,10.262"}},function(t,e,n){"use strict";function r(t,e){if(!(t instanceof e))throw new TypeError("Cannot call a class as a function")}Object.defineProperty(e,"__esModule",{value:!0});var i=n(5),o=n(2),a=n(0),c=function(){function t(t,e){for(var n=0;n<e.length;n++){var r=e[n];r.enumerable=r.enumerable||!1,r.configurable=!0,"value"in r&&(r.writable=!0),Object.defineProperty(t,r.key,r)}}return function(e,n,r){return n&&t(e.prototype,n),r&&t(e,r),e}}(),u=function(){function t(e,i){r(this,t),this.container=e,this.options=i,this.countersLeft=0,this.buttons=[],t.deprecationShown||(console.warn('LIKELY DEPRECATION: Class "likely_visible" will be removed and joined with likely_ready. Button tags will be changed from <div> to <button>.'),t.deprecationShown=!0),n.i(a.toArray)(this.container.children).forEach(this.addButton.bind(this)),this.appear(),this.options.counters?this.readyDelay=setTimeout(this.ready.bind(this),this.options.timeout):this.ready(),this.materializeButtons()}return c(t,[{key:"addButton",value:function(t){var e=new i.a(t,this,this.options);e.isConnected()?(this.buttons.push(e),e.options.service.counterUrl&&this.countersLeft++):e.isUnrecognized()&&console.warn("A button without a valid service detected, please check button classes.")}},{key:"materializeButtons",value:function(){this.buttons.forEach(function(t){return t.prepare()})}},{key:"update",value:function(t){(t.forceUpdate||t.url&&t.url!==this.options.url)&&(this.countersLeft=this.buttons.length,this.buttons.forEach(function(e){e.update(t)}))}},{key:"finalize",value:function(){0===--this.countersLeft&&(clearTimeout(this.readyDelay),this.ready())}},{key:"appear",value:function(){this.container.classList.add(o.default.name+"_visible")}},{key:"ready",value:function(){this.container.classList.add(o.default.name+"_ready")}}]),t}();e.default=u},function(t,e){},function(t,e){var n;n=function(){return this}();try{n=n||Function("return this")()||(0,eval)("this")}catch(t){"object"==typeof window&&(n=window)}t.exports=n},function(t,e,n){var r=n(4);window.addEventListener("load",function(){r.initiate()}),t.exports=r}])});
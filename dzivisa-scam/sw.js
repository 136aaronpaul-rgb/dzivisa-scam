self.addEventListener('install',e=>{e.waitUntil(caches.open('dzivisa').then(c=>c.addAll(['./'])));self.skipWaiting();});
self.addEventListener('fetch',e=>{e.respondWith(caches.match(e.request).then(r=>r||fetch(e.request)));});

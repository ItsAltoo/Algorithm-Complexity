// Import modul os
const os = require('os');

// Menampilkan versi Node.js
console.log(`Versi Node.js: ${process.version}`);

// Menampilkan versi engine V8
console.log(`Versi Engine V8: ${process.versions.v8}`);

// Menampilkan platform dan rilis OS
console.log(`Sistem Operasi: ${os.platform()} ${os.release()}`);

// Output Contoh:
// Versi Node.js: v20.5.0
// Versi Engine V8: 11.3.244.8-node.17
// Sistem Operasi: darwin 22.6.0
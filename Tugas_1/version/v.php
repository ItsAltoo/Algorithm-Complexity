<?php

// Menampilkan versi engine PHP (Zend Engine)
echo "Versi PHP: " . phpversion() . "\n";
// Alternatif: echo "Versi PHP: " . PHP_VERSION . "\n";

// Menampilkan informasi sistem operasi
echo "Sistem Operasi: " . php_uname() . "\n";
// Alternatif: echo "Sistem Operasi: " . PHP_OS . "\n";

// Menampilkan informasi engine
echo "Engine: " . php_sapi_name() . "\n";

// Output Contoh:
// Versi PHP: 8.2.7
// Sistem Operasi: Linux hostname 5.15.0-78-generic #85-Ubuntu SMP Fri Jul 7 15:25:09 UTC 2023 x86_64
<?php

// Membaca file JSON
$jsonContent = file_get_contents('data.json');
$data = json_decode($jsonContent, true)['data'];

function linear_search($arr, $target) {
    $start_time = microtime(true); // Mulai mengukur waktu
    
    for ($i = 0; $i < count($arr); $i++) {
        if ($arr[$i] === $target) {
            $end_time = microtime(true); // Selesai mengukur waktu
            return [
                'index' => $i,
                'time' => ($end_time - $start_time) * 1000 // Konversi ke milliseconds
            ];
        }
    }
    
    $end_time = microtime(true); // Selesai mengukur waktu (jika tidak ditemukan)
    return [
        'index' => -1,
        'time' => ($end_time - $start_time) * 1000 // Konversi ke milliseconds
    ];
}

$result = linear_search($data, 70); // Mencari angka yang sama seperti di JavaScript dan Python
echo "Index found: " . $result['index'] . "\n";
echo "Execution time: " . number_format($result['time'], 6) . " milliseconds\n";

$target = [70, 125, 713, 593, 119, 427, 842, 20, 29, 623];

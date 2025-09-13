<!-- php_benchmark.php -->
<?php
function linear_search($arr, $target) {
    foreach ($arr as $i => $v) {
        if ($v === $target) return $i;
    }
    return -1;
}

function find_min_max($arr) {
    $min = $arr[0];
    $max = $arr[0];
    $min_index = 0;
    $max_index = 0;

    foreach ($arr as $i => $v) {
        if ($v < $min) {
            $min = $v;
            $min_index = $i;
        }
        if ($v > $max) {
            $max = $v;
            $max_index = $i;
        }
    }
    return [$min, $min_index, $max, $max_index];
}

$N = 100000;
$ITER = 10000;
$arr = range(0, $N-1);
mt_srand(0);
$targets = [];
for ($i = 0; $i < $ITER; $i++) $targets[] = mt_rand(0, $N-1);

// Mencari nilai min dan max
list($min, $min_index, $max, $max_index) = find_min_max($arr);
echo "\nPHP :";
echo "\nNilai terkecil: $min pada index: $min_index\n";
echo "Nilai terbesar: $max pada index: $max_index\n\n";

$min_time = PHP_FLOAT_MAX;
$max_time = PHP_FLOAT_MIN;
$min_target = 0;
$max_target = 0;

// Mencari waktu minimum dan maximum untuk setiap pencarian
foreach ($targets as $target) {
    $start_time = hrtime(true);
    $index = linear_search($arr, $target);
    $end_time = hrtime(true);
    $search_time = ($end_time - $start_time) / 1e6; // Convert to milliseconds
    
    if ($search_time < $min_time) {
        $min_time = $search_time;
        $min_target = $target;
    }
    if ($search_time > $max_time) {
        $max_time = $search_time;
        $max_target = $target;
    }
}

echo "\nPencarian tercepat:\n";
echo "Target: $min_target\n";
echo "Waktu: " . number_format($min_time, 6) . " ms\n";
echo "Index: " . linear_search($arr, $min_target) . "\n";

echo "\nPencarian terlama:\n";
echo "Target: $max_target\n";
echo "Waktu: " . number_format($max_time, 6) . " ms\n";
echo "Index: " . linear_search($arr, $max_target) . "\n";

// Mengukur total waktu untuk semua pencarian
$start_total = hrtime(true);
foreach ($targets as $target) {
    linear_search($arr, $target);
}
$end_total = hrtime(true);

$total_s = ($end_total - $start_total) / 1e9; // Convert to seconds
echo "\ntotal $total_s avg " . ($total_s / $ITER) . PHP_EOL;
?>

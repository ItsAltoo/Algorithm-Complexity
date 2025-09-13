// node_benchmark.js
const { performance } = require("perf_hooks");

function linearSearch(arr, target) {
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === target) return i;
  }
  return -1;
}

function findMinMax(arr) {
  let min = arr[0];
  let max = arr[0];
  let minIndex = 0;
  let maxIndex = 0;

  for (let i = 1; i < arr.length; i++) {
    if (arr[i] < min) {
      min = arr[i];
      minIndex = i;
    }
    if (arr[i] > max) {
      max = arr[i];
      maxIndex = i;
    }
  }
  return { min, minIndex, max, maxIndex };
}

const N = 100000;
const ITER = 10000;
const arr = Array.from({ length: N }, (_, i) => i);
const targets = [];
for (let i = 0; i < ITER; i++) targets.push(Math.floor(Math.random() * N));

// Mencari nilai min dan max
const { min, minIndex, max, maxIndex } = findMinMax(arr);
console.log("\nJavaScript :");
console.log(`\nNilai terkecil: ${min} pada index: ${minIndex}`);
console.log(`Nilai terbesar: ${max} pada index: ${maxIndex}\n`);

// warm-up
for (let i = 0; i < 100; i++) linearSearch(arr, targets[i]);


let minTime = Infinity;
let maxTime = -Infinity;
let minTarget = 0;
let maxTarget = 0;

// Mencari waktu minimum dan maximum untuk setiap pencarian
for (const target of targets) {
  const startTime = performance.now();
  const index = linearSearch(arr, target);
  const endTime = performance.now();
  const searchTime = endTime - startTime;

  if (searchTime < minTime) {
    minTime = searchTime;
    minTarget = target;
  }
  if (searchTime > maxTime) {
    maxTime = searchTime;
    maxTarget = target;
  }
}

console.log(`\nPencarian tercepat:`);
console.log(`Target: ${minTarget}`);
console.log(`Waktu: ${minTime.toFixed(6)} ms`);
console.log(`Index: ${linearSearch(arr, minTarget)}`);

console.log(`\nPencarian terlama:`);
console.log(`Target: ${maxTarget}`);
console.log(`Waktu: ${maxTime.toFixed(6)} ms`);
console.log(`Index: ${linearSearch(arr, maxTarget)}`);

const t0 = performance.now();
for (const t of targets) linearSearch(arr, t);
const t1 = performance.now();
const total = (t1 - t0) / 1000; // convert ms to s
console.log("\ntotal", total, "avg", total / ITER);

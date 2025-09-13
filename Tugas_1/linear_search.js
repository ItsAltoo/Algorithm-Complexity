const fs = require("fs");

// Membaca file JSON
const jsonData = fs.readFileSync("data.json");
const data = JSON.parse(jsonData).data;

const linear_search = (arr, target) => {
  const startTime = performance.now(); // Mulai mengukur waktu

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === target) {
      const endTime = performance.now(); // Selesai mengukur waktu
      const executionTime = endTime - startTime;
      return { index: i, time: executionTime };
    }
  }

  const endTime = performance.now(); // Selesai mengukur waktu (jika tidak ditemukan)
  const executionTime = endTime - startTime;
  return { index: -1, time: executionTime };
};

const result = linear_search(data, 345);
console.log(`Index found: ${result.index}`);
console.log(`Execution time: ${result.time.toFixed(6)} milliseconds`);

const target = [70, 125, 713, 593, 119, 427, 842, 20, 29, 623];

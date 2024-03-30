const scores = [68, 95, 54, 84, 77, 75, 63, 74, 69, 80, 71, 63];
let passCount = 0;

for (const score in scores) {
    if (score > 70) {
        passCount++;
    }

}

console.log(passCount);
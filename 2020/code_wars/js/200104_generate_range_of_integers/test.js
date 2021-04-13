function generateRange(min, max, step) {
    let temp = []
    for (let i = min; i <= max; i += step) {
        temp.push(i);
    }
    return temp
}

function generateRange(min, max, step) {
    return Array.from({ length: 1 + (max - min) / step }, (_, i) => min + i * step);
}

test("genrateRange", () => {
    expect(generateRange(2, 10, 2)).toStrictEqual([2, 4, 6, 8, 10])
})
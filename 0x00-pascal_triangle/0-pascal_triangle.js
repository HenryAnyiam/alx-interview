export default function pascal_triangle(n) {
    const triangle = [];
    if (n > 0){
        triangle.push([1]);
        n = n - 1;
        for (let i = 0; i < n; i++) {
            const next = [];
            let currVal = 0;
            const currPascal = triangle[i];
            let length = currPascal.length
            for (let j = 0; j < length; j++) {
                next.push(currVal + currPascal[j]);
                currVal = currPascal[j];
            }
            next.push(currVal + 0);
            triangle.push(next);
        }
    }
    return triangle;
}

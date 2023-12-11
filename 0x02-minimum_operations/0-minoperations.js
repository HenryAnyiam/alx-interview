function is_prime(number) {
    if (number < 2) {
        return false;
    }
    let root = Math.floor(number ** 0.5);
    let divisor = 2
    while (divisor <= root) {
        if ((number % divisor) === 0) {
            return false;
        }
        divisor++;
    }
    return true;
}

function lowest_divisor(number) {
    if (number < 2) {
        return 1;
    }
    let root = Math.floor(number ** 0.5);
    let divisor = 2
    while (divisor <= root) {
        if ((number % divisor) === 0) {
            return divisor;
        }
        divisor++;
    }
    return number;
}

export default function minOperations(n) {
    if (n < 2) {
        return 0;
    }

    let totalOperaton = 0;
    let divided = n;
    let divisor;
    while (is_prime(divided) === false) {
        divisor = lowest_divisor(divided);
        divided = Math.floor(divided / divisor);
        totalOperaton += divisor;
    }
    totalOperaton += divided;
    return totalOperaton;
}
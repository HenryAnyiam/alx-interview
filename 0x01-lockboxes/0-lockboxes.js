export default function canUnlockAll(boxes) {
    if (!(Array.isArray(boxes))) {
        return false;
    }
    const length = boxes.length;
    const unlocked = [0];

    for (let i = 0; i < length; i++) {
        if (Array.isArray(boxes[i])) {
            for (let key of boxes[i]) {
                if ((key < length) && (key !== i) && (!(key in unlocked))) {
                    unlocked.push(key);
                }
            }
        }
    }
    if (unlocked.length !== length) {
        return false
    }
    return true;
}
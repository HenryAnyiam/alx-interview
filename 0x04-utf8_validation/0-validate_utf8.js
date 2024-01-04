function check_data(start, end, arr) {
  while (start < end) {
    if (!(arr[start] >= 128 && arr[start] <= 191)) {
      return false;
    }
    start += 1;
  }
}


function validUTF8(data) {
  let length = data.length;
  let i = 0;

  while (i < length) {
    if (data[i] > 255) {
      return false;
    }

    if (data[i] <= 127) {
      i += 1
    } else if (data[i] >= 192 && data[i] <= 223) {
      if ((i + 2) >= length || !(check_data((i + 1), (i + 2), data))) {
	return false
      }
      i += 2
    } else if (data[i] >= 224 && data[i] <= 239) {
      if ((i + 3) >= length || !(check_data((i + 1), (i + 3), data))) {
	return false;
      }
      i += 3
    } else if (data[i] >= 240 && data[i] <= 247) {
      if ((i + 4) >= length || !(check_data((i + 1), (i + 4), data))) {
	return false;
      }
      i += 4
    } else {
      return false
    }
  }
  return true
}

module.exports = { validUTF8 }

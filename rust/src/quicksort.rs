use rand::prelude::*;

fn quicksort(mut arr: &mut Vec<u32>, length: usize) {
    quicksort_helper(arr, 0, length);
}

fn quicksort_helper(mut arr: &mut Vec<u32>, low: usize, high: usize) {
    if high - low > 1 {
        // pick a pivot and swap with rightmost element
        let mut rng = thread_rng();
        let p_idx: usize = rng.gen_range(low, high);
        let pivot = arr[p_idx];
        arr[p_idx] = arr[high - 1];
        arr[high - 1] = pivot;
        let mut partition: usize = low;

        for i in low..high - 1 {
            if arr[i] < pivot {
                let temp = arr[i];
                arr[i] = arr[partition];
                arr[partition] = temp;
                partition += 1;
            }
        }
        arr[high - 1] = arr[partition];
        arr[partition] = pivot;

        quicksort_helper(arr, low, partition);
        quicksort_helper(arr, partition + 1, high);
    }
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn empty_vec() {
        let mut arr = Vec::new();
        let len = arr.len();
        quicksort(&mut arr, len);
        assert_eq!(arr, vec![]);
    }

    #[test]
    fn one_item() {
        let mut arr = vec![1];
        let len = arr.len();
        quicksort(&mut arr, len);
        assert_eq!(arr, vec![1]);
    }

    #[test]
    fn reverse() {
        let mut arr = vec![5, 4, 2, 1, 0];
        let len = arr.len();
        quicksort(&mut arr, len);
        assert_eq!(arr, vec![0, 1, 2, 4, 5]);
    }

    #[test]
    fn scrambled() {
        let mut arr = vec![4, 2, 5, 1, 0];
        let len = arr.len();
        quicksort(&mut arr, len);
        assert_eq!(arr, vec![0, 1, 2, 4, 5]);
    }

}

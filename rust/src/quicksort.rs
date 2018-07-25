use rand::prelude::*;

fn quicksort(mut arr: &mut Vec<u32>) {
    quicksort_helper(arr, 0, arr.len())
}

fn quicksort_helper(mut arr: &mut Vec<u32>, low: usize, high: usize) {
    if high - low < 2 {
        return;
    }
    // pick a pivot and swap with rightmost element
    let mut rng = thread_rng();
    let p_idx: usize = rng.gen_range(low, high);
    let pivot = arr[p_idx];
    arr[p_idx] = arr[high - 1];
    arr[high - 1] = pivot;
    let partition: usize = low;

    for i in (low..high - 1) {

    }
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn empty_vec() {
        let mut arr = Vec::new();
        quicksort(&mut arr);
        assert_eq!(arr, vec![]);
    }

    #[test]
    fn one_item() {
        let mut arr = vec![1];
        quicksort(&mut arr);
        assert_eq!(arr, vec![1]);
    }

    #[test]
    fn reverse() {
        let mut arr = vec![5, 4, 2, 0];
        quicksort(&mut arr);
        assert_eq!(arr, vec![0, 2, 4, 5]);
    }

    #[test]
    fn scrambled() {
        let mut arr = vec![4, 2, 5, 1, 0];
        quicksort(&mut arr);
        assert_eq!(arr, vec![0, 1, 2, 4, 5]);
    }

}

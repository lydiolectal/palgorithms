#[cfg(test)]

fn quicksort(mut arr: &Vec<u32>){

}

fn quicksort_helper(mut arr: &Vec<u32>) {

}

mod test {
    use super::*;

    #[test]
    fn empty_vec() {
        let mut arr = Vec::new();
        quicksort(&arr);
        assert_eq!(arr, vec![]);
    }

    #[test]
    fn one_item() {
        let mut arr = vec![1];
        quicksort(&arr);
        assert_eq!(arr, vec![1]);
    }

    #[test]
    fn reverse() {
        let mut arr = vec![5, 4, 2, 0];
        quicksort(&arr);
        assert_eq!(arr, vec![0, 2, 4, 5]);
    }

}

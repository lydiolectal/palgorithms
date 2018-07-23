#[cfg(test)]

fn quicksort(arr: Vec<u32>) -> Vec<u32> {
    arr
}

mod test {
    use super::*;

    #[test]
    fn empty_vec() {
        let arr = Vec::new();
        assert_eq!(quicksort(arr), vec![]);
    }

    #[test]
    fn one_item() {
        let arr = vec![1];
        assert_eq!(quicksort(arr), vec![1]);
    }

    #[test]
    fn reverse() {
        let arr = vec![5, 4, 2, 0];
        assert_eq!(quicksort(arr), vec![0, 2, 4, 5]);
    }

}

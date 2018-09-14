pub struct MinHeap {
    size: usize,
    v: Vec<u32>,
}

impl MinHeap {
    pub fn new() -> MinHeap {
        let v: Vec<u32> = vec![0];
        MinHeap { size: 0, v }
    }

    fn insert(&mut self, val: u32) {
        self.v.push(val);
        self.size += 1;
        if self.size == 1 {
            return;
        }
        let mut idx = self.size;
        while idx > 1 {
            let parent_idx = self.size / 2;
            if self.v[parent_idx] > val {
                self.v[idx] = self.v[parent_idx];
                self.v[parent_idx] = val;
                idx = parent_idx;
            } else {
                break;
            }
        }
    }

    fn extract_min(&mut self) -> Option<u32> {
        if self.size == 0 {
            None
        } else {
            let min = self.v[1];
            let last = self.v.pop().unwrap();
            self.size -= 1;
            if self.size > 0 {
                self.v[1] = last;
                let mut idx = 1;
                loop {
                    let child_idx = idx * 2;
                    // no children
                    if child_idx > self.size {
                        break;
                    }
                    // left child
                    else if child_idx + 1 > self.size {
                        if last > self.v[child_idx] {
                            self.v[idx] = self.v[child_idx];
                            self.v[child_idx] = last;
                            idx = child_idx
                        } else {
                            break;
                        }
                    }
                    // both children
                    else {
                        let mut min_idx = child_idx;
                        if self.v[child_idx + 1] < self.v[child_idx] {
                            min_idx = child_idx + 1;
                        }

                        if last > self.v[min_idx] {
                            self.v[idx] = self.v[min_idx];
                            self.v[min_idx] = last;
                            idx = min_idx;
                        } else {
                            break;
                        }
                    }
                }
            }
            Some(min)
        }
    }

    fn peek(&mut self) -> Option<u32> {
        if self.size == 0 {
            None
        } else {
            Some(self.v[1])
        }
    }
}

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn create_minheap() {
        let mut heap = MinHeap::new();
        let expected = 0;
        let result = heap.size;
        assert_eq!(result, expected);
    }

    #[test]
    fn extract_empty() {
        let mut heap = MinHeap::new();
        let expected = None;
        let result = heap.extract_min();
        assert_eq!(result, expected);
    }

    #[test]
    fn insert() {
        let mut heap = MinHeap::new();
        heap.insert(5);
        heap.insert(2);
        heap.insert(1);
        let expected = vec![0, 1, 5, 2];
        assert_eq!(heap.v, expected);
    }

    #[test]
    fn peek() {
        let mut heap = MinHeap::new();
        heap.insert(5);
        heap.insert(2);
        heap.insert(1);
        let expected = 1;
        let result = heap.peek();
        assert_eq!(result.unwrap(), expected);
    }

    #[test]
    fn extract_min() {
        let mut heap = MinHeap::new();
        heap.insert(5);
        heap.insert(2);
        heap.insert(1);
        heap.insert(3);

        let mut result = Vec::new();
        while let Some(val) = heap.extract_min() {
            result.push(val);
        }
        let expected = vec![1, 2, 3, 5];
        assert_eq!(result, expected);
    }
}

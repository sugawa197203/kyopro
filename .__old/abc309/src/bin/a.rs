use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        _a: i32,
        _b: i32,
    }

    if _a % 3 == 1 {
        if _b == _a + 1 {
            println!("Yes");
        } else {
            println!("No");
        }
    } else if _a % 3 == 2 {
        if _b == _a - 1 || _b == _a + 1 {
            println!("Yes");
        } else {
            println!("No");
        }
    } else {
        if _b == _a - 1 {
            println!("Yes");
        } else {
            println!("No");
        }
    }
}

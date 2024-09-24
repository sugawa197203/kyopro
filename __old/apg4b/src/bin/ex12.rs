use proconio::{fastout, input};

#[allow(non_snake_case)]
#[fastout]
fn main() {
    input! {
        S: String
    }

    let mut plusflag = true;
    let mut result = 0;

    for s in S.chars() {
        if s == '1' {
            if plusflag {
                result += 1;
            } else {
                result -= 1;
            }
        } else if s == '+' {
            plusflag = true;
        } else {
            plusflag = false;
        }
    }

    println!("{}", result);
}

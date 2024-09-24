use proconio::{fastout, input};

#[fastout]
#[allow(non_snake_case)]
fn main() {
    input! {
        _A: i32,
        _op: String,
        _B: i32,
    }

    let mut result = 0;
    let mut flag = false;

    match _op.as_str() {
        "+" => result = _A + _B,
        "-" => result = _A - _B,
        "*" => result = _A * _B,
        "/" => {
            result = {
                if _B == 0 {
                    flag = true;
                    0
                } else {
                    _A / _B
                }
            }
        }
        _ => flag = true,
    }

    if flag {
        println!("error");
        return;
    }
    println!("{}", result);
}

use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        _n: usize,
        _k: i128,
        mut _ab: [(i128, i128); _n],
    }

    let mut sum = _ab.iter().map(|x| x.1).sum::<i128>();
    let mut lastday = 0;

    _ab.sort_by(|a, b| a.0.cmp(&b.0));

    for _abs in _ab {
        if sum <= _k {
            println!("{}", lastday + 1);
            break;
        }

        lastday = _abs.0;
        sum -= _abs.1;
    }
}

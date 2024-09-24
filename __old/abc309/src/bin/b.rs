use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        _n: usize,
        _a: [String; _n],
    }

    let mut _newa: Vec<Vec<char>> = Vec::new();
    let mut _aa: Vec<Vec<char>> = Vec::new();

    let _nn = _n - 1;

    for _i in 0.._n {
        _newa.push(_a[_i].chars().collect());
        _aa.push(_a[_i].chars().collect());
    }

    for _i in 0.._nn {
        _newa[0][_i + 1] = _aa[0][_i];
    }

    for _i in 0.._nn {
        _newa[_i + 1][_nn] = _aa[_i][_nn];
    }

    for _i in 0.._nn {
        _newa[_nn][_nn - _i - 1] = _aa[_nn][_nn - _i];
    }

    for _i in 0.._nn {
        _newa[_nn - _i - 1][0] = _aa[_nn - _i][0];
    }

    for _i in 0.._n {
        println!("{}", _newa[_i].iter().collect::<String>());
    }
}

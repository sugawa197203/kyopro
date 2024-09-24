use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: usize,
    }

    let m: usize = 90_000;
    let mut time: Vec<bool> = vec![false; m];

    for _ in 0..n {
        input! {
            ins: String,
        }

        let mut sp = ins.split('-');
        let _s = sp.next().unwrap();
        let _e = sp.next().unwrap();
        let mut s = _s.parse::<usize>().unwrap();
        let mut e = _e.parse::<usize>().unwrap();

        s = (s / 100 * 60 + s % 100) / 5 * 5;
        e = (e / 100 * 60 + e % 100 + 4) / 5 * 5;

        for i in s..e {
            time[i] = true;
        }
    }

    let mut flg = false;
    for i in 0..m {
        if time[i] {
            if !flg {
                print!("{:04}-", i / 60 * 100 + i % 60);
            }
        } else {
            if flg {
                println!("{:04}", i / 60 * 100 + i % 60);
            }
        }
        flg = time[i];
    }
}

use proconio::{fastout, input};

#[allow(non_snake_case)]
#[fastout]
fn main() {
    input! {
        N: usize,
        M: usize,
    }

    let mut P = Vec::<i32>::new();
    let mut C = Vec::<i32>::new();

    let mut F = vec![vec![-1; M]; N];

    for i in 0..N {
        input! {
            p: i32,
            c: i32,
        }

        P.push(p);
        C.push(c);

        for j in 0..c {
            input! {
                f: i32,
            }

            F[i as usize][j as usize] = f;
        }
    }

    for i in 0..N {
        for j in 0..N {
            if i == j {
                continue;
            }

            if P[i] < P[j] {
                continue;
            }

            let mut flag = false;
            for k in 0..C[i] {
                let f = F[i as usize][k as usize];
                if i == 3 && j == 0 {
                    eprintln!("{}", C[i]);
                    eprintln!("{:?}", F[j]);
                    eprintln!("{:?}", F[i]);
                }
                if F[j].iter().any(|&x| x == f) {
                    if i == 3 && j == 0 {
                        eprintln!("{} {} {}", i, j, f);
                    }
                    continue;
                }
                flag = true;
                break;
            }

            if flag {
                continue;
            }

            if P[i] > P[j] {
                println!("Yes");
                eprintln!("Yes1 {} {}", i, j);
                return;
            } else if C[j] > C[i] {
                println!("Yes");
                eprintln!("Yes2 {} {}", i, j);
                return;
            }
        }
    }
    println!("No");
}

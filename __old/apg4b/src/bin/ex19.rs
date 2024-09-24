use proconio::{fastout, input};

#[allow(non_snake_case)]
#[fastout]
fn main() {
    input! {
        mut kuku: [[i32; 9]; 9],
    }

    let mut correct = 0;
    let mut wrong = 0;

    for i in 0..9 {
        for j in 0..9 {
            if kuku[i as usize][j as usize] == (i + 1) * (j + 1) {
                correct += 1;
            } else {
                wrong += 1;
                kuku[i as usize][j as usize] = (i + 1) * (j + 1);
            }
        }
    }

    for line in kuku {
        println!(
            "{}",
            line.iter()
                .map(|x| x.to_string())
                .collect::<Vec<String>>()
                .join(" ")
        );
    }
    println!("{}", correct);
    println!("{}", wrong);
}

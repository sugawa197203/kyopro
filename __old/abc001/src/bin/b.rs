use proconio::{input, fastout};

#[fastout]
fn main() {
    input! {
        m: f32,
    }

    let km = m / 1000.0;

    if km < 0.1 {
        println!("00");
    } else if km <= 5.0 {
        println!("{:02}", (km * 10.0) as i32);
    } else if km <= 30.0 {
        println!("{}", (km + 50.0) as i32);
    } else if km <= 70.0 {
        println!("{}", ((km - 30.0) / 5.0 + 80.0) as i32);
    } else {
        println!("89");
    }
}

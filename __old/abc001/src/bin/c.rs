use proconio::{input, fastout};
 
#[fastout]
fn main() {
	input!{
		deg:usize,
		dis:usize,
	}
	
	let lg = vec!["NNE","NE","ENE","E","ESE","SE","SSE","S","SSW","SW","WSW","W","WNW","NW","NNW","N"];
	let ls = vec![3,16,34,55,80,108,139,172,208,245,285,327];
 
	let mut w = 0;
	let n:i32 = (dis as f64 / 60.0 * 10.0).round() as i32;
	for i in ls {
		if n >= i { w += 1; }
		else { break; }
	}
 
	let mut dir = "N";
	if w == 0 { dir = "C"; }
	else if deg * 10 > 1125 { dir = lg[(deg * 10 - 1125) / 2250]; }
 
	println!("{} {}", dir, w);
}
const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const x = (n)=>{
  if (n === 0){
    return 1
  }else{
    return x(n-1)*n
  }
}
rl.on("line", (n) => {
  console.log(x(parseInt(n)));
  rl.close()
});

rl.on("close", () => {
  process.exit();
});

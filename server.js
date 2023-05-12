const express= require('express');
const { spawn } = require("child_process");
const cors=require('cors')
const bodyParser = require("body-parser");
const fs = require('fs');
const timers = require('timers-promises')

const app=express()
const port=4000;

app.use(express.static('public'))
app.use(express.json()) ;
app.use(cors());
app.use(bodyParser.urlencoded({extended:true}));


app.post('/', (req, res) => {
  // console.log("lol");
   const python = spawn("python", ["main.py", req.body.parcel]);
   python.stdout.on("data", function (data) {
    // processed_data = data.toString();
    console.error(`stdout: ${data}`);

});
python.stderr.on("data", data => {
    console.error(`stderr: ${data}`);
})
    
res.json({ "name": "GeeksforGeeks" });
  });
app.get('/',(req,res)=>{

    const fs = require('fs/promises');

    async function example() {
      try {
        await timers.setTimeout(3000)
        const data = await fs.readFile('C:/Users/91884/OneDrive/Desktop/Regna/tc2.txt', { encoding: 'utf8' });
        console.log("get=>"+data);
        res.send(data)
      } catch (err) {
        console.log(err);
      }
    }
    
    //setTimeout(example,3000);
    example();

    

// fs.readFile('C:/Users/91884/OneDrive/Desktop/Regna/tc.txt', 'utf8', (err, data) => {
//   if (err) {
//     console.error(err);
//     return;
//   }
//   res.send(data)
// });
    
})

app.listen(port);
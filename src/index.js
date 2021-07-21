import React, {useState} from 'react';
import ReactDOM from 'react-dom';
import Query from '/Users/antonioonwu/stonkstop/src/Components/Query.js'
import Result from '/Users/antonioonwu/stonkstop/src/Components/Result.js'
import MostMentioned from './Components/MostMentioned.js'
import 'semantic-ui-css/semantic.min.css'
import {StyledBody, StyledHeader, StyledBack} from '/Users/antonioonwu/stonkstop/src/Style.js';
import Amplify from "aws-amplify";
import awsExports from "./aws-exports";
Amplify.configure(awsExports);


const Stonkstop = () => {
  const [stock,setStock] = useState('')
      return (
        <StyledBody> 
        <div>

<StyledHeader><StyledBack><span>Welcome to Stonk</span><span style={{color: '#ff0404'}}>Stop</span></StyledBack></StyledHeader>

         <Query setStock ={setStock}/>

          <Result stock ={stock}/>
          
          <MostMentioned stock = {stock}/> 
        </div>
        </StyledBody>
      );
  }
  
  // ========================================
  
  ReactDOM.render(
    <Stonkstop/>,
    document.getElementById('root')
  );
  


     

  
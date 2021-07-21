import React, {useState} from 'react';
import AllMentions from '/Users/antonioonwu/stonkstop/src/Backend/AllMentions.json'
import { Dropdown } from 'semantic-ui-react'
import {Rotate,} from '/Users/antonioonwu/stonkstop/src/Style.js';


const Query = ({setStock}) =>{
  const [loading,setLoading] = useState(true);
  const onSubmit = (e, {value}) => {setStock({value})

{

  // puts users queried stock into json file
  fetch('/api/query', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      content: value
    })
  })
  setLoading(false)
  // puts the results from user's query in json file
    fetch('/api/results', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
    })
}
}
    return (
     
      <>
   <Dropdown
    placeholder='Search For A Mentioned Stock'
    fluid
    search
    selection
    options={AllMentions}
    onChange={onSubmit}/>

     {loading ? onSubmit: <Rotate><h7> <img src= "DogeLoad.png" 
     alt=""
     width="15%"
     height= "10%"/> </h7> </Rotate> }
     
</>
    )
}
 
export default Query;
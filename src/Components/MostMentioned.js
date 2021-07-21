import React,{useEffect} from 'react'
import Topstocks from '/Users/antonioonwu/stonkstop/src/Backend/Topstocks.json'
import {StyledMost,StyledText} from '/Users/antonioonwu/stonkstop/src/Style.js'

const MostMentioned = () =>{
    useEffect(() => {
        fetch('/api/topMentions', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
        })
      },[])
      useEffect(() => {
        fetch('/api/AllMentions', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
        })
      },[])
    return(
        
        <div>
        <StyledText>
        <h2>Top 10 Mentioned Stocks</h2>

 
        </StyledText>
        <h4>/Stock/ &emsp;/ Mentions/ &emsp;/ Rating/</h4>
    
  
  <div>
               <StyledMost>
               {Topstocks.map(post => {
                   return(
                       <>
                       <h5>{post.stock}&emsp;&emsp;&emsp;&emsp;{post.mentions}&emsp;&emsp;&emsp;&emsp;{post.rating}</h5>
                       </>
                   )
               })}
               </StyledMost>
              </div>
        </div>  
    )   
}

export default MostMentioned
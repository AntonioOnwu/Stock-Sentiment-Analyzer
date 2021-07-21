import React from 'react'
import Answer from '/Users/antonioonwu/stonkstop/src/Backend/Result.json'

const Result = () =>{
    return(
        <>
  <h1>You should {Answer[0].rating} {Answer[0].stock}; &thinsp; it has {Answer[0].mentions} mentions on WSB!</h1>
        </>
    )  
}

export default Result
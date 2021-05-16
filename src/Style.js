import styled ,{keyframes} from 'styled-components';

export const StyledBody = styled.body`
background-color:#283c74;
text-align:center;
color: #f8cc2c ;
padding:0.25em;
`
export const StyledHeader = styled.div`
background-color:#6c94d8;
color: #acac9c;
font-size:4em;
height:1em;
padding:1.0em;
border:black;
float:center;
margin:auto;
font-family: Copperplate;
`
export const StyledBack = styled.div`
background-color:black;
height:1.5em;
margin:auto;
width:15em;
`


export const rotate = keyframes`
  from {
    transform: rotate(0deg);
  }

  to {
    transform: rotate(360deg);
  }
`;

export const Rotate = styled.div`
  display: inline-block;
  animation: ${rotate} 2s linear infinite;
  padding: .5rem .5rem;
  font-size: 1.2rem;
`;


export const StyledMost = styled.div`
background-color:white;
color: black;
padding:.25em;
width:30em;
border:black;
float:center;
margin:auto;
border-radius:3em 3em 0em 0em;
`
export const StyledText = styled.div`
color: white;
`


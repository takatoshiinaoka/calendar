let dom = document.querySelector('#root')
let message = "React component page"

function Welcome(){
  return(
    <p>test</p>
  )
}

let el = (
  <div>
    <h3>{message}</h3>
    <Welcome />
  </div>
)

ReactDOM.render(el,dom)
import './App.css'
import UserInput from './Components/UserInput'
import UserList from './Components/UserList'
import ProductInput from './Components/ProductInput'
import ProductList from './Components/ProductList'
import OrderInput from './Components/OrderInput'
import OrderList from './Components/OrderList'
import OrderUnitsPopup from './Components/OrderUnitsPopup'
import { useState } from 'react'

function App() {

  if (!localStorage.getItem("popupView")) {
    localStorage.setItem("popupView", "Invisible");
  }

  const [chosenOrderId, setChosenOrderId] = useState(localStorage.getItem("popupOrderId")? localStorage.getItem("popupOrderId") : "None")


  document.addEventListener('click', (event) => {
    if ((event.target.parentNode.parentNode.classList.contains('orderUnit')) || (event.target.classList.contains('orderUnit')) || (event.target.parentNode.classList.contains('orderUnit') && !event.target.classList.contains('delNum'))) {
      const click_order_id = event.target.parentNode.innerText.match(/ID:\s*(\d+)/)[1];
      setChosenOrderId(click_order_id)
      localStorage.setItem("popupOrderId", click_order_id)
      localStorage.setItem("popupView", "Visible")
    }   
})

  return (
    <div className='general'>

      <OrderUnitsPopup order_id={chosenOrderId}/>

      <OrderInput/>
      <OrderList/>
      
      <UserInput/>
      <UserList/>

      <ProductInput/>
      <ProductList/>

    </div>
  )
}

export default App

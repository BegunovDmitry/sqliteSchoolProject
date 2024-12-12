import { useQuery } from "@tanstack/react-query"
import axios from "axios";

const getProductData = () => {
    return axios.get(`http://127.0.0.1:8000/get_all_products`)
}


function OrderUnitsInput(props) {

    const subHandler = (event) => {
        event.preventDefault();
    
        let chosen_product_id;
    
        data.forEach(element => {
            if (element.product_name == event.target[0].value) {        
                chosen_product_id = element.product_id
            }
        }); 
    
        axios.post(`http://127.0.0.1:8000/add_order_units?order_id=${props.order_id}&product_id=${chosen_product_id}&amount=${event.target[1].value}`)
        location.reload();
    }


    const {data, isLoading, isSuccess} = useQuery({
        queryKey: ["productsList"],
        queryFn: getProductData,
        select: data => data.data
    })

    if (isLoading) {
        return <p>Loading....</p>
    }

    if (isSuccess) {

        const products = data.map((product) => 
            <option value={product.product_name} key={product.product_id}/>
            )

        return (
            <form id="orderUnitsForm" onSubmit={subHandler}>
                <div>
                    <label>Товар:</label>
                    <input type="text" id="productName" name="productName" list="options2" required/><br/>
                    <datalist id="options2">
                        {products}
                    </datalist>
                </div>
                
                <div>
                    <label>Кол-во:</label>
                    <input type="text" id="amount" name="amount" required/><br/>    
                </div>
                
                <div>
                    <input type="submit" value="Отправить"/>
                </div>
            </form>
        )
    }


}

export default OrderUnitsInput
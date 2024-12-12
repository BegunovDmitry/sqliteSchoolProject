import { useQuery } from "@tanstack/react-query"
import axios from "axios";


const getProductData = () => {
    return axios.get(`http://127.0.0.1:8000/get_all_products`)
}

const handleDelete = (event) => {
    const product_field = event.target.parentNode
    product_field.classList.add("deleted")
    const del_product_id = product_field.innerText.match(/ID:\s*(\d+)/)[1];
    axios.delete(`http://127.0.0.1:8000/delete_product/${del_product_id}`)
}

function ProductList() {

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
                        <div className="customer" key={product.product_id}>
                            <div><strong>ID:</strong> {product.product_id}, <strong>Имя:</strong> {product.product_name}, <strong>Price:</strong> {product.product_price}</div>
                            <button className="delNum" onClick={handleDelete}>Удалить</button>
                        </div>
                        )

        return (
            <div className='main'>
                <h1>Список товаров</h1>
                <div id="customerList">
                    {products}
                </div>
            </div>
        )
    }
}

export default ProductList
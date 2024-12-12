import { useQuery } from "@tanstack/react-query"
import axios from "axios";


const getUsersData = () => {
    return axios.get(`http://127.0.0.1:8000/get_all_users`)
}

const handleDelete = (event) => {
    const user_field = event.target.parentNode
    user_field.classList.add("deleted")
    const del_user_id = user_field.innerText.match(/ID:\s*(\d+)/)[1];
    axios.delete(`http://127.0.0.1:8000/delete_user/${del_user_id}`)
}

function UserList() {

    const {data, isLoading, isSuccess} = useQuery({
        queryKey: ["usersList"],
        queryFn: getUsersData,
        select: data => data.data
    })


    if (isLoading) {
        return <p>Loading....</p>
    }

    if (isSuccess) {

        const users = data.map((user) => 
                        <div className="customer" key={user.user_id}>
                            <div><strong>ID:</strong> {user.user_id}, <strong>Имя:</strong> {user.user_name}, <strong>Email:</strong> {user.user_email}, <strong>Адрес:</strong> {user.user_address}</div>
                            <button className="delNum" onClick={handleDelete}>Удалить</button>
                        </div>
                        )

        return (
            <div className='main'>
                <h1>Список заказчиков</h1>
                <div id="customerList">
                    {users}
                </div>
            
                <div id="orderModal" style={{display: "none"}}>
                    <div id="orderContent"></div>
                    <button>Закрыть</button>
                </div>
            </div>
        )
    }
}

export default UserList
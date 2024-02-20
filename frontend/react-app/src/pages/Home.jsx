import { useEffect, useState } from "react"
import axios from "axios"
import User from "../components/User"
import { Link } from "react-router-dom"

function Home ()
{
    const [users, setUsers] = useState( [] )
    async function fetchUsers ()
        {
        const { data } = await axios.get( "https://jsonplaceholder.typicode.com/users" )
        setUsers(data)
        }
    useEffect( () =>
    {
        fetchUsers()
    }, [])
    return (
        <div>
            {
                users.map( (user) => 
                {
                    return (
                        <Link to={`/users/${user?.name}`} key={user?.id}>
                            <User
                                id={user?.id}
                                name={user?.name}
                                email={user?.email}
                                username={user?.username}
                            ></User>
                        </Link>
                    )
                })
            }
        </div>
    )
}

export default Home
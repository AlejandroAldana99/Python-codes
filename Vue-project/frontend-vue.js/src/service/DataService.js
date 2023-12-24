import axios from 'axios'


const API_URL = 'http://localhost:5000/api'


class DataService {

    retrieveOrders(data) {
        return axios.get(`${API_URL}/orders/${data}`);
    }

    retrieveNumber() {
        return axios.get(`${API_URL}/norder`);
    }

    // retrieveUser(id) {
    //     return axios.get(`${API_URL}/users/${id}`);
    // }

    deleteOrder(id) {
        return axios.delete(`${API_URL}/orders/${id}`);
    }

    updateOrder(data) {
        return axios.put(`${API_URL}/orders`, data);
    }

    createOrder(data) {
        return axios.post(`${API_URL}/orders`, data);
    }

}

export default new DataService()
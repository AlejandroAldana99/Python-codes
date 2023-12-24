<template>
  <div class="container">
    <h3></h3>
    <div v-if="message" class="alert alert-success">{{ this.message }}</div>
    <div class="container">
      <table class="table" border ="1">
        <td>
          <tr class="container">
            <th><button class="btn btn-success" v-on:click="refresh('pending')">Pending</button></th>
            <th><button class="btn btn-success" v-on:click="refresh('process')">In Process</button></th>
            <th><button class="btn btn-success" v-on:click="refresh('completed')">Completed</button></th>
            <th><button class="btn btn-success" v-on:click="refresh('delivered')">Delivered</button></th>
            <th><button class="btn btn-success" v-on:click="refresh('canceled')">Canceled</button></th>
          </tr>
        </td>
      </table>
      <br>
      <table >
        <tbody>
          <tr v-for="o in orders" v-bind:key="o.order">
            <td>
              <tr> 
                <td>{{ `Order #${o.order}` }}</td>
                <td>|</td>
                <td>{{ current }}</td>
              </tr>
              <br>
              <tr><p>Products</p></tr>
              <tr v-for="i in o.products" v-bind:key="i.id">
                <td>{{ i.item }} - {{ i.quantity }}</td>
              </tr>
            </td>
            <td>
              <button class="btn btn-warning" v-on:click="update(next, o)">
                {{ next }}
              </button>
            </td>
            <td>
              <button class="btn btn-danger" v-on:click="cancel(o)">
                Cancel
              </button>
            </td>
          </tr>
        </tbody>
      </table>
      <br>
      <div class="row">
        <button class="btn btn-success" v-on:click="addO()">Add</button>
      </div>
    </div>
  </div>
</template>
<script>
import DataService from "../service/DataService";

export default {
  name: "Orders",
  data() {
    return {
      orders: [],
      param: "",
      next: "",
      current: "",
      message: "",
    };
  },
  methods: {
    refresh(param) {
      switch(param) {
        case "pending":
          this.next = "In Process";
          this.current = "Pending";
          break;
        case "process":
          this.next = "Completed";
          this.current = "In Process";
          break;
        case "completed":
          this.next = "Delivered";
          this.current = "Completed";
          break;
        case "delivered":
          this.next = "Finalized";
          this.current = "Delivered";
          break;
        case "canceled":
          this.next = "Delete";
          this.current = "Canceled";
          break;
        default:
          break;
      }

      DataService.retrieveOrders(param).then((res) => {
        this.orders = res.data.data;
      });
    },
    addO() {
      this.$router.push(`/order/-1`);
    },
    update(stt, data) {
      let newStatus = "";
      switch(stt) {
        case "Pending":
          this.param = "pending"
          newStatus = "";
          break;
        case "In Process":
          this.param = "pending"
          newStatus = "process";
          break;
        case "Completed":
          this.param = "process"
          newStatus = "completed";
          break;
        case "Delivered":
          this.param = "completed"
          newStatus = "delivered";
          break;
        case "Finalized":
          this.param = "delivered"
          newStatus = "finalized";
          break;  
        default:
          break;
      }
      if(stt === "Delete") {
        this.param = "canceled";
        let id = data._id; 
        DataService.deleteOrder(id.$oid).then(() => {
          this.refresh(this.param);
        });
      }
      else {
        data.status = newStatus;
        DataService.updateOrder(data).then(() => {
          this.refresh(this.param);
        });
      }
    },
    cancel(data) {
      data.status = "canceled";
      this.param = "canceled";
      DataService.updateOrder(data).then(() => {
        this.refresh(this.param);
      });
    },
  },
};
</script>
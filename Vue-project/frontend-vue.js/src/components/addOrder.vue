<template>
  <div>
    <h3>New Order</h3>
    <div class="container">
        <fieldset class="form-group">
          <label>Number de Orden</label>
          <input type="text" class="form-control" :placeholder="getOrder()" :disabled="true" v-model="order" />
        </fieldset>
        <fieldset class="form-group">
          <label>Estatus</label>
          <input type="text" class="form-control" placeholder="Pending" v-model="status" />
        </fieldset>
        <fieldset class="form-group">
          <label>Contenido</label>
          <table>
            <tbody>
              <tr v-for="i in rowData" v-bind:key="i.id">
                <td><input type="text" class="form-control" placeholder="Item" v-model="i.item" /></td>
                <td><input type="text" class="form-control" placeholder="Quantity" v-model="i.quantity" /></td>
            </tr>
            </tbody>
          </table>
          <br>
          <button class="btn btn-secondary" v-on:click="addCurrent()">Add +</button>
        </fieldset>
        <form @submit="validateAndSubmit">
          <div v-if="errors.length">
            <div
              class="alert alert-danger"
              v-bind:key="index"
              v-for="(error, index) in errors"
            >
              {{ error }}
            </div>
          </div>
          <button class="btn btn-success" type="submit">Save</button>
      </form>
    </div>
  </div>
</template>
<script>
import DataService from "../service/DataService";

export default {
  name: "Order",
  data() {
    return {
      order: "",
      status: "",
      next: "",
      items: {
        id: 0,
        item: "",
        quantity: 0,
      },
      errors: [],
      rowData:[],
    };
  },
  computed: {
    id() {
      return this.$route.params.id;
    },
  },
  methods: {
    getOrder() {
      DataService.retrieveNumber().then((res) => {
        this.order = res.data.n || 0;
      });
    },
    addCurrent() {
      this.items.id = this.items.id + 1;
      this.rowData.push(JSON.parse(JSON.stringify(this.items)));
    },
    validateAndSubmit(e) {
      e.preventDefault();
      let statusValid = ['Pending', 'Completed', 'In Process', 'Delivered'];
      this.errors = [];
      if (!this.order) {
        this.errors.push("Enter valid values");
      }
      if (!this.status) {
        this.errors.push("Enter valid values");
      }
      if (!statusValid.includes(this.status)) {
        this.errors.push("Enter valid values")
      }
      if (this.errors.length === 0) {
        switch(this.status) {
          case "Pending":
            this.next = "pending";
            break;
          case "In Process":
            this.next = "process";
            break;
          case "Completed":
            this.next = "completed";
            break;
          case "Delivered":
            this.next = "delivered";
            break;
          default:
            break;
        }
        this.rowData.slice(0);
        DataService.createOrder({
          order: this.order,
          status: this.next,
          products: this.rowData,
        }).then(() => {
          this.$router.push("/");
        });
      }
    },
  },
  // created() {
  //   this.refreshUserDetails();
  // },
};
</script>

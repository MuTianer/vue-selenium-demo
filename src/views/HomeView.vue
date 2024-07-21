<template>
  <div class="home-layout">
    <Navbar />
    <div class="main-content">
      <Sidebar />
      <div id="home-welcome" class="content-area">
        <h1>Welcome, {{ userStore.user?.username }}</h1>
        <p>
          This is your home dashboard. Here you can see an overview of your activities and manage
          your account.
        </p>

        <div class="cards-container">
          <InfoCard title="Card 1" description="This is the description for card 1">
            <el-button type="primary">Action 1</el-button>
          </InfoCard>
          <InfoCard title="Card 2" description="This is the description for card 2">
            <el-button type="primary">Action 2</el-button>
          </InfoCard>
          <InfoCard title="Card 3" description="This is the description for card 3">
            <el-button type="primary">Action 3</el-button>
          </InfoCard>
        </div>

        <div class="details-container">
          <h2>Details Section</h2>
          <el-table :data="tableData">
            <el-table-column prop="date" label="Date" width="180"></el-table-column>
            <el-table-column prop="name" label="Name" width="180"></el-table-column>
            <el-table-column prop="address" label="Address"></el-table-column>
          </el-table>
        </div>
      </div>
    </div>
    <footer class="footer">© 2024 Your Company. All rights reserved.</footer>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import Navbar from '../components/Navbar.vue'
import Sidebar from '../components/Sidebar.vue'
import InfoCard from '../components/InfoCard.vue'
import { useUserStore } from '../store'

export default defineComponent({
  components: {
    Navbar,
    Sidebar,
    InfoCard
  },
  setup() {
    const userStore = useUserStore()

    const tableData = [
      {
        date: '2024-07-01',
        name: 'John Doe',
        address: '123 Main St'
      },
      {
        date: '2024-07-02',
        name: 'Jane Smith',
        address: '456 Oak St'
      },
      {
        date: '2024-07-03',
        name: 'Sam Johnson',
        address: '789 Pine St'
      }
    ]

    return {
      userStore,
      tableData
    }
  }
})
</script>

<style scoped>
.home-layout {
  display: flex;
  flex-direction: column;
  height: 100vh;
}

.main-content {
  display: flex;
  flex: 1;
}

.content-area {
  flex: 1;
  padding: 20px;
}

.cards-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
}

.details-container {
  margin-top: 20px;
}

.footer {
  text-align: center;
  padding: 10px 0;
  background: #f5f5f5;
  border-top: 1px solid #eaeaea;
}
</style>

import './App.css';
import { Routes, Route, Navigate } from "react-router-dom";
import { connect } from 'react-redux';
// import RouteGuard from './RouterGuard';
// import AuthLayout from './layout/Auth/index';
// import Admin from './layout/Admin';
// import { history } from './reduxStore/store';
import LoginScreen from './pages/AuthScreens/Login';
import SignUpScreen from './pages/AuthScreens/SignUp';
import Home from './pages/Home';
import RouterGuard from './components/RouterGuard';
import Layout from './components/Layout';
import ForgotPassScreen from './pages/AuthScreens/ForgotPassword';
import ResetPasswordScreen from './pages/AuthScreens/ResetPassword';
import { Toaster } from 'react-hot-toast';

function App() {
  // const { loginInfo } = props;

  return (
    <div className="App">
      <Toaster position='top-center' />
      <Routes>
        <Route element={<Layout />}>
          <Route path="/login" element={<LoginScreen />} />
          <Route path="/signup" element={<SignUpScreen />} />
          <Route path="/forgot-pass" element={<ForgotPassScreen />} />
          <Route path="/reset-pass" element={<ResetPasswordScreen />} />
          <Route element={<RouterGuard />}>
            <Route path="/home" element={<Home />} />
          </Route>
          <Route path="/*" element={<Navigate to="/login" replace />} />
        </Route>
      </Routes>
    </div>
  );
}

const mapStateToProps = (state) => ({
  loginInfo: state.login.loginInfo,
});

export default connect(mapStateToProps, null)(App);

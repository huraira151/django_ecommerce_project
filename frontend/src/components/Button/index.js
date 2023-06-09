import React from 'react';
import { Spinner } from 'react-bootstrap';
import Image from '../Image';
import CircularProgress from '@mui/material/CircularProgress';


// Style
import './style.scss';

const Button = ({
  title = '',
  className = '',
  loading = '',
  showIcon,
  showSpinner,
  src,
  onClick,
  type,
  ...props
}) => {
  const iconSrc = showIcon ? showIcon : false;
  const spinner = showSpinner ? showSpinner : false;
  return (
    <button
      className={`lukymoon-btn ${className}`}
      onClick={onClick}
      disabled={props.disabled || props.loading}
      type={type}>
      {iconSrc && (
        <span className="icon">
          <Image src={src} />
        </span>
      )}
      <span className="title-text" title={title}>
        {title}
      </span>
      {spinner && (
        <CircularProgress sx={{color: "#FFFFFF", marginLeft: "5px"}} size={18} />
      )}
    </button>
  );
};

export default Button;

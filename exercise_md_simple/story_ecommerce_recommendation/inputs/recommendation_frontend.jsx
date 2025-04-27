import React, { useState, useEffect, useCallback } from 'react';
import PropTypes from 'prop-types';
import axios from 'axios';

// 样式
const styles = {
  container: {
    margin: '20px 0',
    fontFamily: 'Arial, sans-serif',
  },
  header: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: '15px',
  },
  title: {
    fontSize: '18px',
    fontWeight: 'bold',
    color: '#333',
    margin: 0,
  },
  listContainer: {
    position: 'relative',
    overflow: 'hidden',
  },
  list: {
    display: 'flex',
    overflowX: 'auto',
    padding: '5px 0',
    scrollBehavior: 'smooth',
    msOverflowStyle: 'none',  /* IE and Edge */
    scrollbarWidth: 'none',   /* Firefox */
    '&::-webkit-scrollbar': {
      display: 'none',        /* Chrome, Safari, Opera */
    },
  },
  item: {
    flex: '0 0 auto',
    width: '180px',
    marginRight: '15px',
    padding: '10px',
    border: '1px solid #eee',
    borderRadius: '4px',
    transition: 'transform 0.3s, box-shadow 0.3s',
    cursor: 'pointer',
    position: 'relative',
    backgroundColor: '#fff',
    '&:hover': {
      transform: 'translateY(-5px)',
      boxShadow: '0 5px 15px rgba(0,0,0,0.1)',
    },
  },
  image: {
    width: '100%',
    height: '180px',
    objectFit: 'contain',
    marginBottom: '10px',
    backgroundColor: '#f9f9f9',
  },
  name: {
    fontSize: '14px',
    fontWeight: 'normal',
    margin: '0 0 5px 0',
    color: '#333',
    height: '40px',
    overflow: 'hidden',
    textOverflow: 'ellipsis',
    display: '-webkit-box',
    WebkitLineClamp: 2,
    WebkitBoxOrient: 'vertical',
  },
  price: {
    fontSize: '16px',
    fontWeight: 'bold',
    color: '#e53935',
    margin: '0 0 5px 0',
  },
  originalPrice: {
    fontSize: '12px',
    color: '#999',
    textDecoration: 'line-through',
    marginLeft: '5px',
  },
  reason: {
    fontSize: '12px',
    color: '#757575',
    margin: '0',
  },
  navigationButton: {
    position: 'absolute',
    top: '50%',
    transform: 'translateY(-50%)',
    width: '40px',
    height: '40px',
    backgroundColor: 'rgba(255, 255, 255, 0.8)',
    border: 'none',
    borderRadius: '50%',
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    boxShadow: '0 2px 5px rgba(0,0,0,0.15)',
    cursor: 'pointer',
    zIndex: 1,
  },
  prevButton: {
    left: '5px',
  },
  nextButton: {
    right: '5px',
  },
  skeleton: {
    backgroundColor: '#f0f0f0',
    backgroundImage: 'linear-gradient(90deg, #f0f0f0, #f8f8f8, #f0f0f0)',
    backgroundSize: '200px 100%',
    backgroundRepeat: 'no-repeat',
    backgroundPosition: 'left -40px top 0',
    animation: 'shimmer 1.5s infinite',
    height: '100%',
    width: '100%',
    borderRadius: '4px',
  },
  skeletonItem: {
    flex: '0 0 auto',
    width: '180px',
    height: '280px',
    marginRight: '15px',
    borderRadius: '4px',
  },
  error: {
    padding: '20px',
    color: '#e53935',
    textAlign: 'center',
    border: '1px solid #ffcdd2',
    borderRadius: '4px',
    backgroundColor: '#ffebee',
  },
  emptyState: {
    padding: '20px',
    textAlign: 'center',
    color: '#757575',
  },
  '@keyframes shimmer': {
    '0%': {
      backgroundPosition: 'left -40px top 0',
    },
    '100%': {
      backgroundPosition: 'right -40px top 0',
    },
  },
};

// 定义内联样式函数
const inlineStyles = {
  container: {
    margin: '20px 0',
    fontFamily: 'Arial, sans-serif',
  },
  header: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: '15px',
  },
  title: {
    fontSize: '18px',
    fontWeight: 'bold',
    color: '#333',
    margin: 0,
  },
  listContainer: {
    position: 'relative',
    overflow: 'hidden',
  },
  list: {
    display: 'flex',
    overflowX: 'auto',
    padding: '5px 0',
    scrollBehavior: 'smooth',
    msOverflowStyle: 'none',
    scrollbarWidth: 'none',
  },
  item: {
    flex: '0 0 auto',
    width: '180px',
    marginRight: '15px',
    padding: '10px',
    border: '1px solid #eee',
    borderRadius: '4px',
    transition: 'transform 0.3s, box-shadow 0.3s',
    cursor: 'pointer',
    position: 'relative',
    backgroundColor: '#fff',
  },
  itemHover: {
    transform: 'translateY(-5px)',
    boxShadow: '0 5px 15px rgba(0,0,0,0.1)',
  },
  image: {
    width: '100%',
    height: '180px',
    objectFit: 'contain',
    marginBottom: '10px',
    backgroundColor: '#f9f9f9',
  },
  name: {
    fontSize: '14px',
    fontWeight: 'normal',
    margin: '0 0 5px 0',
    color: '#333',
    height: '40px',
    overflow: 'hidden',
    textOverflow: 'ellipsis',
    display: '-webkit-box',
    WebkitLineClamp: 2,
    WebkitBoxOrient: 'vertical',
  },
  price: {
    fontSize: '16px',
    fontWeight: 'bold',
    color: '#e53935',
    margin: '0 0 5px 0',
  },
  originalPrice: {
    fontSize: '12px',
    color: '#999',
    textDecoration: 'line-through',
    marginLeft: '5px',
  },
  reason: {
    fontSize: '12px',
    color: '#757575',
    margin: '0',
  },
  navigationButton: (position) => ({
    position: 'absolute',
    top: '50%',
    transform: 'translateY(-50%)',
    [position]: '5px',
    width: '40px',
    height: '40px',
    backgroundColor: 'rgba(255, 255, 255, 0.8)',
    border: 'none',
    borderRadius: '50%',
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    boxShadow: '0 2px 5px rgba(0,0,0,0.15)',
    cursor: 'pointer',
    zIndex: 1,
  }),
  skeleton: {
    backgroundColor: '#f0f0f0',
    height: '100%',
    width: '100%',
    borderRadius: '4px',
  },
  skeletonItem: {
    flex: '0 0 auto',
    width: '180px',
    height: '280px',
    marginRight: '15px',
    borderRadius: '4px',
  },
  error: {
    padding: '20px',
    color: '#e53935',
    textAlign: 'center',
    border: '1px solid #ffcdd2',
    borderRadius: '4px',
    backgroundColor: '#ffebee',
  },
  emptyState: {
    padding: '20px',
    textAlign: 'center',
    color: '#757575',
  },
};

// 骨架屏组件
const SkeletonItem = () => (
  <div style={inlineStyles.skeletonItem}>
    <div style={inlineStyles.skeleton}></div>
  </div>
);

// 推荐项组件
const RecommendationItem = ({ item, onClick }) => {
  const [isHovered, setIsHovered] = useState(false);
  
  const itemStyle = {
    ...inlineStyles.item,
    ...(isHovered ? inlineStyles.itemHover : {})
  };

  return (
    <div 
      style={itemStyle}
      onClick={() => onClick(item)}
      onMouseEnter={() => setIsHovered(true)}
      onMouseLeave={() => setIsHovered(false)}
    >
      <img 
        src={item.image_url} 
        alt={item.name} 
        style={inlineStyles.image}
        onError={(e) => {
          e.target.src = 'https://via.placeholder.com/180x180?text=No+Image';
        }}
      />
      <h3 style={inlineStyles.name}>{item.name}</h3>
      <p style={inlineStyles.price}>
        ¥{item.price.toFixed(2)}
        {item.original_price && (
          <span style={inlineStyles.originalPrice}>¥{item.original_price.toFixed(2)}</span>
        )}
      </p>
      {item.reason && <p style={inlineStyles.reason}>{item.reason}</p>}
    </div>
  );
};

RecommendationItem.propTypes = {
  item: PropTypes.shape({
    item_id: PropTypes.string.isRequired,
    name: PropTypes.string.isRequired,
    image_url: PropTypes.string.isRequired,
    price: PropTypes.number.isRequired,
    original_price: PropTypes.number,
    reason: PropTypes.string,
  }).isRequired,
  onClick: PropTypes.func.isRequired,
};

// 主推荐组件
const RecommendationContainer = ({ 
  title = '推荐商品',
  userId,
  sceneId,
  itemId,
  categoryId,
  count = 10,
  apiUrl = '/api/recommendations',
  onItemClick
}) => {
  const [recommendations, setRecommendations] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const listRef = useRef(null);

  // 获取推荐数据
  useEffect(() => {
    const fetchRecommendations = async () => {
      try {
        setLoading(true);
        setError(null);

        const response = await axios.post(apiUrl, {
          user_id: userId,
          scene_id: sceneId,
          item_id: itemId,
          category_id: categoryId,
          count: count
        });

        if (response.data && response.data.recommendations) {
          setRecommendations(response.data.recommendations);
        } else {
          setRecommendations([]);
        }
      } catch (err) {
        console.error('Error fetching recommendations:', err);
        setError('无法加载推荐内容，请稍后再试');
      } finally {
        setLoading(false);
      }
    };

    fetchRecommendations();
  }, [apiUrl, userId, sceneId, itemId, categoryId, count]);

  // 处理项点击
  const handleItemClick = useCallback((item) => {
    if (onItemClick) {
      onItemClick(item);
    } else {
      // 默认行为：跳转到商品详情页
      window.location.href = `/product/${item.item_id}`;
    }
  }, [onItemClick]);

  // 左右滚动控制
  const scroll = useCallback((direction) => {
    if (listRef.current) {
      const { scrollLeft, clientWidth } = listRef.current;
      const scrollAmount = direction === 'left' ? -clientWidth : clientWidth;
      listRef.current.scrollBy({ left: scrollAmount, behavior: 'smooth' });
    }
  }, []);

  // 渲染内容
  const renderContent = () => {
    if (loading) {
      return (
        <div style={inlineStyles.list}>
          {Array(5).fill().map((_, index) => (
            <SkeletonItem key={index} />
          ))}
        </div>
      );
    }

    if (error) {
      return <div style={inlineStyles.error}>{error}</div>;
    }

    if (recommendations.length === 0) {
      return <div style={inlineStyles.emptyState}>暂无推荐内容</div>;
    }

    return (
      <div style={inlineStyles.listContainer}>
        <button 
          style={inlineStyles.navigationButton('left')}
          onClick={() => scroll('left')}
          aria-label="Previous"
        >
          &lt;
        </button>
        <div style={inlineStyles.list} ref={listRef}>
          {recommendations.map(item => (
            <RecommendationItem
              key={item.item_id}
              item={item}
              onClick={handleItemClick}
            />
          ))}
        </div>
        <button 
          style={inlineStyles.navigationButton('right')}
          onClick={() => scroll('right')}
          aria-label="Next"
        >
          &gt;
        </button>
      </div>
    );
  };

  return (
    <div style={inlineStyles.container}>
      <div style={inlineStyles.header}>
        <h2 style={inlineStyles.title}>{title}</h2>
      </div>
      {renderContent()}
    </div>
  );
};

RecommendationContainer.propTypes = {
  title: PropTypes.string,
  userId: PropTypes.string.isRequired,
  sceneId: PropTypes.string.isRequired,
  itemId: PropTypes.string,
  categoryId: PropTypes.string,
  count: PropTypes.number,
  apiUrl: PropTypes.string,
  onItemClick: PropTypes.func,
};

// 提供不同场景的推荐组件
export const HomePageRecommendations = (props) => (
  <RecommendationContainer 
    title="为您推荐" 
    sceneId="home"
    {...props}
  />
);

export const ProductDetailRecommendations = ({ productId, ...props }) => (
  <RecommendationContainer 
    title="相关推荐" 
    sceneId="detail"
    itemId={productId}
    {...props}
  />
);

export const CartRecommendations = (props) => (
  <RecommendationContainer 
    title="购物车推荐" 
    sceneId="cart"
    {...props}
  />
);

export const CategoryRecommendations = ({ categoryId, ...props }) => (
  <RecommendationContainer 
    title="分类推荐" 
    sceneId="category"
    categoryId={categoryId}
    {...props}
  />
);

export default RecommendationContainer; 
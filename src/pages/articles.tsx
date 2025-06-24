import { useEffect, useState } from 'react';
import { LikeOutlined, MessageOutlined, StarOutlined } from '@ant-design/icons';
import { ProList } from '@ant-design/pro-components';
import request from 'umi-request'; 
import React from 'react';

const IconText = ({ icon, text }: { icon: any; text: string }) => (
  <span>
    {React.createElement(icon, { style: { marginInlineEnd: 8 } })}
    {text}
  </span>
);


interface Article {
  id: string;
  title: string;
  summary: string; // 摘要信息
  content: string;
  createdAt: string;
  // 根据你的接口返回数据结构添加其他属性
}

export default ()=>{

  const [articles, setArticles] = useState<Article[]>([]);

  const fetchData = async () => {
    try {
      const response = await request('/articles/list');
      setArticles(response); // 假设接口返回的数据是一个文章数组
      console.log("result:", response);
    } catch (error) {
      console.error('Failed to fetch articles:', error);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  return (
    <ProList<Article>
      itemLayout="vertical"
      headerTitle="安全知识早餐"
      dataSource={articles}
      metas={{
        title: {
          dataIndex: 'title',
        },
        description: {
          dataIndex: 'summary',
        },
        actions: {
          render: () => [
            <IconText
              icon={StarOutlined}
              text="156"
              key="list-vertical-star-o"
            />,
            <IconText
              icon={LikeOutlined}
              text="156"
              key="list-vertical-like-o"
            />,
            <IconText
              icon={MessageOutlined}
              text="2"
              key="list-vertical-message"
            />,
          ],
        },
        extra: {
          render: () => (
            <img
              width={272}
              alt="logo"
              src="https://gw.alipayobjects.com/zos/rmsportal/mqaQswcyDLcXyDKnZfES.png"
            />
          ),
        },
        content: {
          dataIndex: 'content',
          render: (item) => {
            return (
              <div>
                {item}段落示意：蚂蚁金服设计平台
                design.alipay.com，用最小的工作量，无缝接入蚂蚁金服生态，提供跨越设计与开发的体验解决方案。蚂蚁金服设计平台
              </div>
            );
          }
        },
        // 可以添加更多列
      }}
    />
  );
};
